"""Financial institution client model."""

from email_validator import validate_email


class Client:
    """Represent a financial institution client and their contact details."""

    def __init__(self, client_id: int, name: str, email_address: str) -> None:
        """Create a client after validating its identifier, name, and email."""
        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero")
        self.__client_id = client_id
        self.__name = self._normalize_name(name)
        self.__email_address = self._normalize_email(email_address)

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Trim a name and reject it if no characters remain."""
        normalized = name.strip()
        if not normalized:
            raise ValueError("name cannot be an empty string")
        return normalized

    @staticmethod
    def _normalize_email(email_address: str) -> str:
        """Return the validator's normalized email without checking deliverability."""
        # Deliverability depends on DNS and is outside this model's validation rules.
        return validate_email(email_address.strip(), check_deliverability=False).normalized

    @property
    def client_id(self) -> int:
        """Return the client's unique identifier."""
        return self.__client_id

    @property
    def name(self) -> str:
        """Return the client's trimmed name."""
        return self.__name

    @property
    def email_address(self) -> str:
        """Return the normalized email address."""
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        """Validate and normalize a replacement email address."""
        self.__email_address = self._normalize_email(email_address)

    def __str__(self) -> str:
        """Return the client name, client number, and email address."""
        return f"{self.__name} [{self.__client_id}] - {self.__email_address}"
