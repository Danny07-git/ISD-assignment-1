
"""
Defines the Client class.

A Client represents a customer of a financial institution.
Client information includes a unique identifier, name,
and validated email address.
"""

from email_validator import validate_email, EmailNotValidError


class Client:
    """Represents a financial institution's client."""

    def __init__(
        self,
        client_id: int,
        name: str,
        email_address: str
    ):
        """
        Initialize a Client instance.

        Args:
            client_id: Unique client identifier.
            name: Client's full name.
            email_address: Client's email address.

        Raises:
            ValueError: If the client ID is invalid or name is empty.
            EmailNotValidError: If the email address is invalid.
        """

        if client_id <= 0:
            raise ValueError(
                "client_id must be a value greater than zero"
            )

        name = name.strip()

        if not name:
            raise ValueError(
                "name cannot be an empty string"
            )

        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_address

        # Validate and normalize the email address.
        self.email_address = email_address

    @property
    def client_id(self) -> int:
        """Return the client's unique identifier."""
        return self.__client_id

    @property
    def name(self) -> str:
        """Return the client's name."""
        return self.__name

    @property
    def email_address(self) -> str:
        """Return the client's normalized email address."""
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        """
        Validate and update the client's email address.

        Args:
            email_address: New email address.

        Raises:
            EmailNotValidError: If the email address is invalid.
        """

        email_address = email_address.strip()

        validated_email = validate_email(
            email_address,
            check_deliverability=False
        )

        self.__email_address = validated_email.normalized

    def __str__(self) -> str:
        """Return a formatted string representation of the client."""

        return (
            f"{self.__name} [{self.__client_id}] - "
            f"{self.__email_address}"
        )
