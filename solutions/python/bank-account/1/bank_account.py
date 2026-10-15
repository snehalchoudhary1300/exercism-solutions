
"""Manage bank accounts."""


class BankAccount:
    """Represent a bank account with basic operations."""

    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        """Return the account balance."""
        if not self.is_open:
            raise ValueError("account not open")
        return self.balance

    def open(self):
        """Open the account."""
        if self.is_open:
            raise ValueError("account already open")

        self.is_open = True
        self.balance = 0

    def deposit(self, amount):
        """Deposit money into the account."""
        if not self.is_open:
            raise ValueError("account not open")

        if amount <= 0:
            raise ValueError("amount must be greater than 0")

        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if not self.is_open:
            raise ValueError("account not open")

        if amount <= 0:
            raise ValueError("amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("amount must be less than balance")

        self.balance -= amount

    def close(self):
        """Close the account."""
        if not self.is_open:
            raise ValueError("account not open")

        self.is_open = False
        self.balance = None
