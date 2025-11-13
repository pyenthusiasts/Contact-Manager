"""
Unit tests for validation module.
"""

import pytest
from contact_manager.validation import validate_email, validate_phone, sanitize_input


class TestEmailValidation:
    """Test cases for email validation."""

    def test_valid_emails(self):
        """Test valid email addresses."""
        valid_emails = [
            "test@example.com",
            "user.name@example.com",
            "user+tag@example.co.uk",
            "user123@test-domain.com"
        ]
        for email in valid_emails:
            assert validate_email(email), f"Expected {email} to be valid"

    def test_invalid_emails(self):
        """Test invalid email addresses."""
        invalid_emails = [
            "",
            "invalid",
            "@example.com",
            "user@",
            "user @example.com",
            "user@.com"
        ]
        for email in invalid_emails:
            assert not validate_email(email), f"Expected {email} to be invalid"


class TestPhoneValidation:
    """Test cases for phone validation."""

    def test_valid_phones(self):
        """Test valid phone numbers."""
        valid_phones = [
            "123-456-7890",
            "(123) 456-7890",
            "123.456.7890",
            "1234567890",
            "+1 123 456 7890",
            "+44 20 1234 5678"
        ]
        for phone in valid_phones:
            assert validate_phone(phone), f"Expected {phone} to be valid"

    def test_invalid_phones(self):
        """Test invalid phone numbers."""
        invalid_phones = [
            "",
            "123",  # Too short
            "abc-def-ghij",  # No digits
            "12345678901234567890"  # Too long
        ]
        for phone in invalid_phones:
            assert not validate_phone(phone), f"Expected {phone} to be invalid"


class TestSanitizeInput:
    """Test cases for input sanitization."""

    def test_sanitize_whitespace(self):
        """Test whitespace removal."""
        assert sanitize_input("  test  ") == "test"
        assert sanitize_input("\ntest\t") == "test"

    def test_sanitize_empty(self):
        """Test empty input handling."""
        assert sanitize_input("") is None
        assert sanitize_input("   ") is None
        assert sanitize_input(None) is None

    def test_sanitize_valid(self):
        """Test valid input."""
        assert sanitize_input("test") == "test"
