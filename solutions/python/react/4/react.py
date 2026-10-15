
"""Implement a basic reactive system."""


class InputCell:
    """A cell whose value can be changed directly."""

    def __init__(self, initial_value):
        self._value = initial_value
        self.compute_cells = []

    @property
    def value(self):
        """Return the current value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Update the value and propagate changes."""
        if self._value == new_value:
            return

        self._value = new_value
        _update_cells(self.compute_cells)


class ComputeCell:
    """A cell whose value depends on other cells."""

    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.compute_cells = []
        self._value = compute_function(
            [cell.value for cell in inputs]
        )

        for input_cell in inputs:
            input_cell.compute_cells.append(self)

    @property
    def value(self):
        """Return the current computed value."""
        return self._value

    def update_value(self):
        """Recalculate this cell's value."""
        self._value = self.compute_function(
            [cell.value for cell in self.inputs]
        )

    def add_callback(self, callback):
        """Register a callback."""
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        """Remove a registered callback."""
        if callback in self.callbacks:
            self.callbacks.remove(callback)


def _update_cells(start_cells):
    """Recalculate dependent cells before notifying callbacks."""
    pending = list(start_cells)
    affected = []
    seen = set()

    while pending:
        cell = pending.pop(0)

        if cell in seen:
            continue

        seen.add(cell)
        affected.append(cell)
        pending.extend(cell.compute_cells)

    old_values = {cell: cell.value for cell in affected}
    remaining = set(affected)

    while remaining:
        ready = [
            cell for cell in remaining
            if all(
                not isinstance(input_cell, ComputeCell)
                or input_cell not in remaining
                for input_cell in cell.inputs
            )
        ]

        if not ready:
            break

        for cell in ready:
            cell.update_value()
            remaining.remove(cell)

    for cell in affected:
        if old_values[cell] != cell.value:
            for callback in cell.callbacks[:]:
                callback(cell.value)
