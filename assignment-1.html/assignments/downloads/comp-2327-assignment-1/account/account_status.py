"""Possible states for a bank account."""

from enum import Enum


class AccountStatus(Enum):
    """Lifecycle status assigned to a bank account."""

    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
