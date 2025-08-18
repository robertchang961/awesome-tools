"""SSH client module for paramiko-based SSH operations.

This module provides the SSHClient class for connecting to SSH servers,
executing commands, and managing connection parameters using paramiko.
"""

import atexit
import time
from ipaddress import IPv4Address

import paramiko


class SSHClient:
    """SSH client class for paramiko-based SSH operations.

    This class provides methods for connecting to an SSH server, running commands,
    and managing connection parameters.

    Attributes:
        _host (str): The SSH server host (IPv4).
        _username (str): The SSH username.
        _password (str): The SSH password.
        _port (int): The SSH server port. Defaults to 22.
        exit_status (int | None): Previous exit status of run method.
    """

    def __init__(self, host: str, username: str, password: str, port: int = 22) -> None:
        """Initialize SSHClient instance.

        Sets up the paramiko SSH client and initializes connection parameters.
        """
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self.exit_status = None    # previous exit status of run method

    @property
    def host(self) -> str:
        """Get the SSH server host.

        Returns:
            host (str | None): The SSH server host (IPv4 address).
        """
        return self._host

    @host.setter
    def host(self, host: str) -> None:
        """Set the SSH server host.

        Args:
            host (str): The SSH server host (IPv4 address).

        Raises:
            ipaddress.AddressValueError: If host is not a valid IPv4 address.
        """
        IPv4Address(host)
        self._host = host

    @property
    def port(self) -> int:
        """Get the SSH server port.

        Returns:
            port (int | None): The SSH server port.
        """
        return self._port

    @port.setter
    def port(self, port: int) -> None:
        """Set the SSH server port.

        Args:
            port (int): The SSH server port.

        Raises:
            ValueError: If port is not an integer between 1 and 65535.
        """
        if not isinstance(port, int) or (not 1 <= port <= 65535):
            raise ValueError("Port must be an integer between 1 and 65535")
        self._port = port

    @property
    def username(self) -> str | None:
        """Get the SSH username.

        Returns:
            username (str | None): The SSH username.
        """
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        """Set the SSH username.

        Args:
            username (str): The SSH username.

        Raises:
            TypeError: If username is not a string.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        self._username = username

    @property
    def password(self) -> str | None:
        """Get the SSH password.

        Returns:
            password (str | None): The SSH password.
        """
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        """Set the SSH password.

        Args:
            password (str): The SSH password.

        Raises:
            TypeError: If password is not a string.
        """
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        self._password = password

    def connect(self) -> None:
        """Connect to the SSH server.

        Registers the close method to be called at exit.
        """
        self.client = paramiko.SSHClient()
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
