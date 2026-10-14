
"""Implement a circular buffer."""


class BufferFullException(BufferError):
    """Exception raised when the circular buffer is full."""


class BufferEmptyException(BufferError):
    """Exception raised when the circular buffer is empty."""


class CircularBuffer:
    """Represent a fixed-size circular buffer."""

    def __init__(self, capacity):
        """Initialize the circular buffer."""
        self.capacity = capacity
        self.buffer = []

    def read(self):
        """Remove and return the oldest item."""
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.pop(0)

    def write(self, data):
        """Add an item unless the buffer is full."""
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data):
        """Add an item, replacing the oldest item if necessary."""
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)

        self.buffer.append(data)

    def clear(self):
        """Remove all items from the buffer."""
        self.buffer.clear()
