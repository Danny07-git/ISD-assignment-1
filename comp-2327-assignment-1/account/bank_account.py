"""Bank account model."""

from decimal import Decimal

from .account_status import AccountStatus
from .client import Client


class BankAccount:
    """Store account ownership, status, and balance operations."""

    def __init__(
        self,
        account_id: int,
        balance: Decimal,
        owner: Client,
        status: AccountStatus,
    ) -> None:
        """Create an account, rejecting identifiers that are not positive."""
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")
        self.__account_id = account_id
        # Convert through str so floats do not import their binary rounding noise.
        self.__balance = Decimal(str(balance))
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        """Return the account's unique identifier."""
        return self.__account_id

    @property
    def balance(self) -> Decimal:
        """Return the current account balance."""
        return self.__balance

    @property
    def owner(self) -> Client:
        """Return the client who owns this account."""
        return self.__owner

    @property
    def status(self) -> AccountStatus:
        """Return the account's current status."""
        return self.__status

    def update_balance(self, amount: Decimal) -> None:
        """Add a signed amount to the balance without applying transaction rules."""
        self.__balance += Decimal(str(amount))

    def deposit(self, amount: Decimal) -> None:
        """Add a non-negative amount to the account balance."""
        amount = Decimal(str(amount))
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")
        self.update_balance(amount)

    def withdraw(self, amount: Decimal) -> None:
        """Subtract a non-negative amount that does not exceed the balance."""
        amount = Decimal(str(amount))
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")
        if amount > self.__balance:
            raise ValueError("amount cannot exceed the account balance")
        self.update_balance(-amount)

    def __str__(self) -> str:
        """Return the account number and currency-formatted balance."""
        return f"Account Number: {self.__account_id} Balance: ${self.__balance:,.2f}"
