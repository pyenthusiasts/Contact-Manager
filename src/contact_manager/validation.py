"""
Input validation utilities.

This module provides validation functions for contact information
such as email addresses and phone numbers.
"""

import re
from typing import Union


def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Parameters
    ----------
    email : str
        The email address to validate.

    Returns
    -------
    bool
        True if the email is valid, False otherwise.
    """
    if not email:
        return False

    # Basic email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Validate a phone number.

    Accepts various formats:
    - 123-456-7890
    - (123) 456-7890
    - 123.456.7890
    - 1234567890
    - +1 123 456 7890

    Parameters
    ----------
    phone : str
        The phone number to validate.

    Returns
    -------
    bool
        True if the phone number is valid, False otherwise.
    """
    if not phone:
        return False

    # Remove all non-digit characters except '+'
    cleaned = re.sub(r'[^\d+]', '', phone)

    # Check if it contains only digits (and optionally a leading '+')
    if not re.match(r'^\+?\d+$', cleaned):
        return False

    # Extract just the digits
    digits = re.sub(r'\D', '', cleaned)

    # Phone number should have between 10 and 15 digits
    return 10 <= len(digits) <= 15


def sanitize_input(text: Union[str, None]) -> Union[str, None]:
    """
    Sanitize user input by stripping whitespace.

    Parameters
    ----------
    text : Union[str, None]
        The text to sanitize.

    Returns
    -------
    Union[str, None]
        The sanitized text or None if input was empty.
    """
    if text is None:
        return None

    text = text.strip()
    return text if text else None
