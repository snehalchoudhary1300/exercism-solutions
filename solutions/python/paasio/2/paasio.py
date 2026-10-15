
"""Track filesystem and network input/output statistics."""

import io


class MeteredFile(io.BufferedRandom):
    """Track file read and write statistics using inheritance."""

    def __init__(self, *args, **kwargs):
        """Initialize the file and its counters."""
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        """Return this file wrapper when entering a context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the file when leaving a context."""
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        """Return an iterator over the file's lines."""
        return self

    def __next__(self):
        """Read and return the next line."""
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def read(self, size=-1):
        """Read data and update read statistics."""
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    def readline(self, size=-1):
        """Read one line and update read statistics."""
        line = super().readline(size)
        self._read_bytes += len(line)
        self._read_ops += 1
        return line

    @property
    def read_bytes(self):
        """Return the total number of bytes read."""
        return self._read_bytes

    @property
    def read_ops(self):
        """Return the total number of read operations."""
        return self._read_ops

    def write(self, b):
        """Write data and update write statistics."""
        written = super().write(b)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def write_bytes(self):
        """Return the total number of bytes written."""
        return self._write_bytes

    @property
    def write_ops(self):
        """Return the total number of write operations."""
        return self._write_ops


class MeteredSocket:
    """Track socket read and write statistics using delegation."""

    def __init__(self, socket):
        """Initialize the socket wrapper and its counters."""
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        """Return this wrapper when entering a context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Delegate context exit to the wrapped socket."""
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        """Receive data and update receive statistics."""
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self):
        """Return the total number of bytes received."""
        return self._recv_bytes

    @property
    def recv_ops(self):
        """Return the total number of receive operations."""
        return self._recv_ops

    def send(self, data, flags=0):
        """Send data and update send statistics."""
        sent = self._socket.send(data, flags)
        self._send_bytes += sent
        self._send_ops += 1
        return sent

    @property
    def send_bytes(self):
        """Return the total number of bytes sent."""
        return self._send_bytes

    @property
    def send_ops(self):
        """Return the total number of send operations."""
        return self._send_ops
