"""Module for managing subprocess execution and network drive mounting.

Provides:
- Subproc: Utility for running shell commands with retry and error handling.
- Mount: Class for mounting network drives and transferring files via SCP.
"""

import atexit
import re
import shlex
import subprocess
import time
from datetime import datetime
from ipaddress import IPv4Address

from pydantic import BaseModel, Field, field_validator


def pt(
    msg: str,
    *,
    is_date: bool = True,
    is_ansicolor: bool = False,
) -> None:
    """Print a message with optional date and ANSI color formatting.

    Args:
        msg (str): The message to print.
        is_date (bool, optional): Whether to prepend the current date. Defaults to True.
        is_ansicolor (bool, optional): Whether to use ANSI color formatting. Defaults to False.
    """
    today = datetime.today().isoformat()
    ansicolor_reset_format = r"\033[0m"
    ansicolor_bold_font = r"\033[1m"
    ansicolor_failed_font = r"\033[38;5;9m"
    if is_date:
        msg = f"[{today}] {msg}"
    if is_ansicolor:
        msg = f"{ansicolor_bold_font}{ansicolor_failed_font}{msg}{ansicolor_reset_format}"
    print(f"{msg}", flush=True)


class Subproc:
    """Run a command in a subprocess."""

    @staticmethod
    def run(
        cmd: str,
        timeout: int = 600,
        shell: bool = False,
        check: bool = True,
        retry: int = 3,
    ) -> str:
        """Run the command in a subprocess and return the output.

        Args:
            cmd (str): The command to execute.
            timeout (int, optional): Timeout in seconds. Defaults to 600.
            shell (bool, optional): Whether to run the command in a shell. Defaults to False.
            check (bool, optional): Raise error if command fails. Defaults to True.
            retry (int, optional): Number of retries if command fails. Defaults to 3.

        Returns:
            stdout_or_stderr (str): The command output (stdout or stderr).

        Raises:
            RuntimeError: If the command fails and check is True.
        """
        for _ in range(retry):
            if shell:
                result = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=timeout,
                    shell=shell,
                )
            else:
                result = subprocess.run(
                    shlex.split(cmd),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=timeout,
                    shell=shell,
                )
            # pt(f"{result.returncode=}, {cmd=}")

            if not check or result.returncode == 0:
                break

            time.sleep(1)

        if check and result.returncode != 0:
            pt(f"Failed to run command: {cmd}", is_ansicolor=True)
            raise RuntimeError(result.stderr)

        if result.returncode != 0:
            return result.stderr
        return result.stdout


class Mount(BaseModel):
    """Add a cmdkey and mount a network drive. Copy files to/from the remote server using SCP.

    Attributes:
        host (str): The host IP address.
        username (str): The username.
        password (str): The password.
        port (int): The port number. Defaults to 22.
        free_letter (str | None): The first available drive letter.
    """

    host: str
    port: int = Field(default=22, ge=1, le=65535)
    username: str
    password: str
    free_letter: str | None = Field(default=None, description="First available drive letter")

    @field_validator("host")
    @classmethod
    def validate_host(cls, value: str) -> str:
        """Validate and convert host to IPv4Address."""
        IPv4Address(value)
        return value

    @field_validator("free_letter")
    @classmethod
    def validate_free_letter(cls, value: str | None) -> str:
        """Validate and convert free_letter to uppercase."""
        print(value)
        if value is None:
            value = cls.get_free_drive_letter()
        return value

    @staticmethod
    def get_free_drive_letter() -> str:
        """Get a free drive letter for Windows.

        Returns:
            free_letter (str): The first available drive letter.

        Raises:
            RuntimeError: If no available drive letters.
        """
        # all possible drive letters A-Z
        all_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # get the list of used drive letters
        result = Subproc.run("wmic logicaldisk get caption")
        used_letters = result.split()

        # remove used letters from the set of all letters
        free_letters = all_letters - {letter.strip(":") for letter in used_letters if ":" in letter}

        # return the first available letter
        if free_letters:
            pt(f"Get free letter: {sorted(free_letters)[0]}")
            return sorted(free_letters)[0]
        else:
            raise RuntimeError("No available drive letters")

    def add_cmdkey(self) -> None:
        """Add the cmdkey for Windows credential manager."""
        shell = " " in self.username or " " in self.password
        ret = Subproc.run(f'cmdkey /list "{self.host}"', check=False)
        Subproc.run(f'cmdkey /delete:"{self.host}"', check=False)
        Subproc.run(f'cmdkey /add:"{self.host}" /user:"{self.username}" /pass:"{self.password}"', shell=shell)
        Subproc.run(f'cmdkey /generic:"{self.host}" /user:"{self.username}" /pass:"{self.password}"', shell=shell)
        pt(f'Add cmdkey "{self.host}" "{self.username}" "{self.password}" successfully')
        if "Generic" in ret and "Domain" in ret:
            return
        atexit.register(self.delete_cmdkey)

    def delete_cmdkey(self) -> None:
        """Delete the cmdkey from Windows credential manager."""
        Subproc.run(f'cmdkey /delete:"{self.host}"')
        pt(f'Delete cmdkey /delete:"{self.host}" successfully')

    def mount(self, sub_folder: str = "Public") -> None:
        """Mount the network drive to a local drive letter.

        Args:
            sub_folder (str, optional): The remote folder to mount. Defaults to Public.
        """
        Subproc.run(rf'net use {self.free_letter}: "\\\\{self.host}\\{sub_folder}"')
        pt(f'net use {self.free_letter}: "\\\\{self.host}\\{sub_folder}" successfully')
        atexit.register(self.umount)

    def umount(self) -> None:
        """Unmount the network drive."""
        Subproc.run(f"net use {self.free_letter}: /delete /y")

    def scp(
        self,
        local_file: str,
        remote_file: str,
        copy_to_remote: bool = True,
    ) -> None:
        """Copy files to/from the remote server using SCP. Local OS is Windows and remote OS is Linux.

        Args:
            local_file (str): The local file path.
            remote_file (str): The remote file path.
            copy_to_remote (bool, optional): If True, copy local_file to remote_file. If False, copy remote_file to local_file. Defaults to True.
        """
        # need to install pscp
        local_file = local_file.replace("\\", "\\\\")
        if copy_to_remote:
            filename = local_file.split("\\")[-1]
        else:
            filename = remote_file.split("/")[-1]

        if copy_to_remote:
            # get the hostkey if it is the first time to connect to the server
            ret = Subproc.run(f'"pscp.exe" -batch -ssh -pw "{self.password}" "{local_file}" "{self.username}"@"{self.host}":"{remote_file}"', check=False)
            hostkey = re.findall(r"ssh-[\w]+ \d+ SHA256:[A-Za-z0-9+/=]+", ret)
            if hostkey:
                hostkey = hostkey[0]
                # subproc.run failed if the hostkey is not found in registry (regedit) and path HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys
                Subproc.run(f'"pscp.exe" -hostkey "{hostkey}" -ssh -pw "{self.password}" "{local_file}" "{self.username}"@"{self.host}":"{remote_file}"')
            Subproc.run(rf'dir "{self.free_letter}:\{filename}"', shell=True)
            pt(f"SCP {local_file} {self.username}@{self.host}:{remote_file} successfully")
        else:
            # get the hostkey if it is the first time to connect to the server
            ret = Subproc.run(f'"pscp.exe" -batch -ssh -pw "{self.password}" "{self.username}"@"{self.host}":"{remote_file}" "{local_file}"', check=False)
            hostkey = re.findall(r"ssh-[\w]+ \d+ SHA256:[A-Za-z0-9+/=]+", ret)
            if hostkey:
                hostkey = hostkey[0]
                # subproc.run failed if the hostkey is not found in registry (regedit) and path HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys
                Subproc.run(f'"pscp.exe" -hostkey "{hostkey}" -ssh -pw "{self.password}" "{self.username}"@"{self.host}":"{remote_file}" "{local_file}"')
            Subproc.run(rf'dir "{local_file}\{filename}"', shell=True)
            pt(f"SCP {self.username}@{self.host}:{remote_file} {local_file} successfully")


if __name__ == "__main__":
    mount_manually = Mount(host="ip", username="username", password="password")
    mount_manually.add_cmdkey()
    mount_nas = Mount(host="ip", username="username", password="password")
    mount_nas.add_cmdkey()
    mount_nas.mount()
    mount_nas.scp(r"C:\Users\DQV5\Downloads\test.txt", "/share/Public/test.txt")
