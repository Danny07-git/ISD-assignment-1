
"""
This first step defines the possible statuses of a bank account.

The AccountStatus enumeration represents the current
operational state of a bank account.
"""

from enum import Enum


class AccountStatus(Enum):
    """Enumeration of possible bank account statuses."""

    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
