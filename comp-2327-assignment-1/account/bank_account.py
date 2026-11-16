"""Bank account model used by the banking system."""

class BankAccount:
    """Represent a customer's bank account."""

    def __init__(self, account_id, balance, owner, status):
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")
        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self):
        """Return the account's unique identifier."""
        return self.__account_id

    @property
    def balance(self):
        """Return the current account balance."""
        return self.__balance

    @property
    def owner(self):
        """Return the account owner."""
        return self.__owner

    @property
    def status(self):
        """Return the account status."""
        return self.__status

    def update_balance(self, amount):
        """Add a signed amount to the balance."""
        self.__balance += amount

    def deposit(self, amount):
        """Deposit a non-negative amount."""
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")
        self.update_balance(amount)

    def withdraw(self, amount):
        """Withdraw an amount that does not exceed the balance."""
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")
        if amount > self.__balance:
            raise ValueError("amount cannot exceed the account balance")
        self.update_balance(-amount)

    def __str__(self):
        return f"Account Number: {self.__account_id} Balance: ${self.__balance:,.2f}"
