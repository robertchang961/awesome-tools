"""SSH client module for paramiko-based SSH operations.

This module provides the SSHClient class for connecting to SSH servers,
executing commands, and managing connection parameters using paramiko.
"""

import atexit
import time
from ipaddress import IPv4Address

import paramiko
from pydantic import BaseModel, ConfigDict, Field, field_validator


class SSHClient(BaseModel):
    """SSH client class for paramiko-based SSH operations.

    This class provides methods for connecting to an SSH server, running commands,
    and managing connection parameters.

    Attributes:
        host (str): The SSH server host (IPv4).
        port (int): The SSH server port. Defaults to 22.
        username (str): The SSH username.
        password (str): The SSH password.
        client (paramiko.SSHClient): The paramiko SSH client instance.
        exit_status (int | None): Previous exit status of run method. Defaults to None.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    host: str
    port: int = Field(default=22, ge=1, le=65535)
    username: str
    password: str
    client: paramiko.SSHClient = Field(default_factory=paramiko.SSHClient)
    exit_status: int | None = Field(default=None, description="Previous exit status of run method")

    @field_validator("host")
    @classmethod
    def validate_host(cls, value: str) -> str:
        """Validate and convert host to IPv4Address."""
        IPv4Address(value)
        return value

    def connect(self) -> None:
        """Connect to the SSH server.

        Registers the close method to be called at exit.
        """
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            timeout=10,
        )
        atexit.register(self.close)

    def close(self) -> None:
        """Close the SSH connection.

        Closes the paramiko SSH client if it exists.
        """
        if self.client:
            self.client.close()

    def run(
        self,
        cmd: str,
        timeout: int = 60,
        retry: int = 3,
        return_err: bool = False,
    ) -> str:
        """Run a command on the SSH server and return the output.

        Args:
            cmd (str): The command to execute on the server.
            timeout (int, optional): Timeout for command execution in seconds. Defaults to 60.
            retry (int, optional): Number of retries if command fails. Defaults to 3.
            return_err (bool, optional): If True, return stderr output. Defaults to False.

        Returns:
            stdout_or_stderr (str): The command output (stdout or stderr).
        """
        for _ in range(retry):
            stdin, stdout, stderr = self.client.exec_command(cmd, timeout=timeout)
            ret = stdout.read().decode("utf-8", errors="ignore")
            ret_err = stderr.read().decode("utf-8", errors="ignore")

            self.exit_status = stdout.channel.recv_exit_status()
            if self.exit_status == 0:
                break

            time.sleep(1)

        # returns stderr if exit status is not equal to 0
        if self.exit_status != 0:
            ret = ret_err

        if return_err:
            return ret_err.strip()

        return ret.strip()
