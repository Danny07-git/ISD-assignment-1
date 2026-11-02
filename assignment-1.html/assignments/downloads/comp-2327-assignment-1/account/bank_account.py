
"""
Defines the BankAccount class.

A BankAccount represents an account held by a client
at a financial institution.
"""

from decimal import Decimal

from account.account_status import AccountStatus
from account.client import Client


class BankAccount:
    """Represents a bank account belonging to a client."""

    def __init__(
        self,
        account_id: int,
        balance: Decimal,
        owner: Client,
        status: AccountStatus
    ):
        """
        Initialize a BankAccount instance.

        Args:
            account_id: Unique account identifier.
            balance: Initial account balance.
            owner: Client who owns the account.
            status: Current account status.

        Raises:
            ValueError: If account_id is less than or equal to zero.
        """

        if account_id <= 0:
            raise ValueError(
                "account_id must be a value greater than zero"
            )

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        """Return the account identifier."""
        return self.__account_id

    @property
    def balance(self) -> Decimal:
        """Return the current account balance."""
        return self.__balance

    @property
    def owner(self) -> Client:
        """Return the account owner."""
        return self.__owner

    @property
    def status(self) -> AccountStatus:
        """Return the current account status."""
        return self.__status

    def update_balance(self, amount: Decimal) -> None:
        """
        Update the account balance by the specified amount.

        Positive amounts increase the balance.
        Negative amounts decrease the balance.

        Args:
            amount: Amount to add to or subtract from the balance.
        """
        self.__balance += amount

    def deposit(self, amount: Decimal) -> None:
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """

        if amount < 0:
            raise ValueError(
                "amount must be a value greater than or equal to zero"
            )

        self.update_balance(amount)

    def withdraw(self, amount: Decimal) -> None:
        """
        Withdraw money from the account.

        Args:
            amount: Amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds
                        the available account balance.
        """

        if amount < 0:
            raise ValueError(
                "amount must be a value greater than or equal to zero"
            )

        if amount > self.__balance:
            raise ValueError(
                "amount cannot exceed the account balance"
            )

        self.update_balance(-amount)

    def __str__(self) -> str:
        """Return a formatted string representation of the account."""

        return (
            f"Account Number: {self.__account_id} "
            f"Balance: ${self.__balance:,.2f}"
        )
