"""
Unit tests for models module.
"""

import pytest
from datetime import datetime
from contact_manager.models import Contact


class TestContact:
    """Test cases for Contact class."""

    def test_create_valid_contact(self):
        """Test creating a valid contact."""
        contact = Contact(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890"
        )
        assert contact.name == "John Doe"
        assert contact.email == "john@example.com"
        assert contact.phone == "123-456-7890"
        assert contact.address is None
        assert contact.notes is None
        assert isinstance(contact.created_at, datetime)
        assert isinstance(contact.updated_at, datetime)

    def test_create_contact_with_optional_fields(self):
        """Test creating a contact with optional fields."""
        contact = Contact(
            name="Jane Doe",
            email="jane@example.com",
            phone="987-654-3210",
            address="123 Main St",
            notes="Important client"
        )
        assert contact.address == "123 Main St"
        assert contact.notes == "Important client"

    def test_invalid_email(self):
        """Test that invalid email raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email"):
            Contact(
                name="Test",
                email="invalid-email",
                phone="123-456-7890"
            )

    def test_invalid_phone(self):
        """Test that invalid phone raises ValueError."""
        with pytest.raises(ValueError, match="Invalid phone"):
            Contact(
                name="Test",
                email="test@example.com",
                phone="123"
            )

    def test_empty_name(self):
        """Test that empty name raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Contact(
                name="",
                email="test@example.com",
                phone="123-456-7890"
            )

    def test_update_contact(self):
        """Test updating contact fields."""
        contact = Contact(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890"
        )

        original_updated_at = contact.updated_at

        # Small delay to ensure timestamp changes
        import time
        time.sleep(0.01)

        contact.update(name="Jane Doe", address="123 Main St")

        assert contact.name == "Jane Doe"
        assert contact.address == "123 Main St"
        assert contact.updated_at > original_updated_at

    def test_to_dict(self):
        """Test converting contact to dictionary."""
        contact = Contact(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890",
            address="123 Main St"
        )

        data = contact.to_dict()

        assert data['name'] == "John Doe"
        assert data['email'] == "john@example.com"
        assert data['phone'] == "123-456-7890"
        assert data['address'] == "123 Main St"
        assert 'created_at' in data
        assert 'updated_at' in data

    def test_from_dict(self):
        """Test creating contact from dictionary."""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890',
            'address': '123 Main St',
            'notes': 'Test notes',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }

        contact = Contact.from_dict(data)

        assert contact.name == "John Doe"
        assert contact.email == "john@example.com"
        assert contact.phone == "123-456-7890"
        assert contact.address == "123 Main St"
        assert contact.notes == "Test notes"

    def test_str_representation(self):
        """Test string representation."""
        contact = Contact(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890"
        )

        str_rep = str(contact)
        assert "John Doe" in str_rep
        assert "john@example.com" in str_rep
        assert "123-456-7890" in str_rep
