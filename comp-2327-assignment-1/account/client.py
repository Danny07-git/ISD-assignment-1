"""Client model and email-address validation."""

from email_validator import EmailNotValidError, validate_email


class Client:
    """Represent a customer of a financial institution."""

    def __init__(self, client_id, name, email_address):
        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero")
        name = name.strip()
        if not name:
            raise ValueError("name cannot be an empty string")
        self.__client_id = client_id
        self.__name = name
        self.__email_address = self._normalize_email(email_address)

    @staticmethod
    def _normalize_email(email_address):
        """Validate an email without checking its deliverability."""
        result = validate_email(email_address.strip(), check_deliverability=False)
        return result.normalized

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.strip()
        if not value:
            raise ValueError("name cannot be an empty string")
        self.__name = value

    @property
    def email_address(self):
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = self._normalize_email(value)

    def __str__(self):
        return f"{self.__name} [{self.__client_id}] - {self.__email_address}"
