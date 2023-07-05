"""
author: Maxim Van den Abeele
06/05/2023
"""
import socket
from enum import Enum


class Commands(Enum):
    """Available commands on ginco bridge"""
    CONFIGURE = 0

class GincoSocket:
    """Class to write data and receive on socket connection to ginco bridge"""

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, hostname: str="192.168.4.1", port: int=30675):
        """Connect to the socket

        Args:
            hostname (str, optional): _description_. Defaults to "192.168.4.1".
            port (int, optional): _description_. Defaults to 30675.
        """
        self._socket.connect((hostname, port))

    def start_command(self, command: Commands):
        """Send command byte to ginco bridge"""
        self._socket.send(self._byte_from_int(command.value))

    def send_string(self, string: str):
        """Send a string of data"""
        self._socket.send(self._byte_from_int(len(string)))
        self._socket.send(string.encode())

    def receive_response(self) -> str:
        """Receive response form ginco bridge"""
        chunk = self._socket.recv(1)
        return chunk.decode()

    def _byte_from_int(self, data: int) -> bytes:
        string = f"\\x{data:02x}"
        return string.encode().decode('unicode_escape').encode("raw_unicode_escape")
