"""
Unit tests for manager module.
"""

import pytest
import tempfile
import os
from contact_manager.models import Contact
from contact_manager.manager import ContactManager


@pytest.fixture
def temp_storage():
    """Create a temporary storage file for testing."""
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
    temp_file.close()
    yield temp_file.name
    # Cleanup
    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)


@pytest.fixture
def manager(temp_storage):
    """Create a ContactManager instance with temporary storage."""
    return ContactManager(temp_storage)


@pytest.fixture
def sample_contact():
    """Create a sample contact for testing."""
    return Contact(
        name="John Doe",
        email="john@example.com",
        phone="123-456-7890"
    )


class TestContactManager:
    """Test cases for ContactManager class."""

    def test_add_contact(self, manager, sample_contact):
        """Test adding a contact."""
        manager.add_contact(sample_contact)
        assert len(manager.contacts) == 1
        assert manager.contacts[0].name == "John Doe"

    def test_add_duplicate_email(self, manager, sample_contact):
        """Test that duplicate email raises ValueError."""
        manager.add_contact(sample_contact)

        duplicate = Contact(
            name="Jane Doe",
            email="john@example.com",  # Same email
            phone="987-654-3210"
        )

        with pytest.raises(ValueError, match="already exists"):
            manager.add_contact(duplicate)

    def test_search_contact_by_name(self, manager, sample_contact):
        """Test searching for contacts by name."""
        manager.add_contact(sample_contact)
        results = manager.search_contact("John")

        assert len(results) == 1
        assert results[0].name == "John Doe"

    def test_search_contact_by_email(self, manager, sample_contact):
        """Test searching for contacts by email."""
        manager.add_contact(sample_contact)
        results = manager.search_contact("john@example")

        assert len(results) == 1
        assert results[0].email == "john@example.com"

    def test_search_contact_case_insensitive(self, manager, sample_contact):
        """Test that search is case-insensitive."""
        manager.add_contact(sample_contact)
        results = manager.search_contact("JOHN")

        assert len(results) == 1

    def test_search_no_results(self, manager):
        """Test search with no results."""
        results = manager.search_contact("nonexistent")
        assert len(results) == 0

    def test_get_contact_by_email(self, manager, sample_contact):
        """Test getting contact by exact email."""
        manager.add_contact(sample_contact)
        contact = manager.get_contact_by_email("john@example.com")

        assert contact is not None
        assert contact.name == "John Doe"

    def test_get_contact_by_email_not_found(self, manager):
        """Test getting contact with non-existent email."""
        contact = manager.get_contact_by_email("nonexistent@example.com")
        assert contact is None

    def test_update_contact(self, manager, sample_contact):
        """Test updating a contact."""
        manager.add_contact(sample_contact)

        success = manager.update_contact(
            "john@example.com",
            name="Jane Doe",
            phone="987-654-3210"
        )

        assert success
        contact = manager.get_contact_by_email("john@example.com")
        assert contact.name == "Jane Doe"
        assert contact.phone == "987-654-3210"

    def test_update_nonexistent_contact(self, manager):
        """Test updating a non-existent contact."""
        success = manager.update_contact(
            "nonexistent@example.com",
            name="Test"
        )
        assert not success

    def test_delete_contact(self, manager, sample_contact):
        """Test deleting a contact."""
        manager.add_contact(sample_contact)
        assert len(manager.contacts) == 1

        success = manager.delete_contact("john@example.com")

        assert success
        assert len(manager.contacts) == 0

    def test_delete_nonexistent_contact(self, manager):
        """Test deleting a non-existent contact."""
        success = manager.delete_contact("nonexistent@example.com")
        assert not success

    def test_get_all_contacts(self, manager, sample_contact):
        """Test getting all contacts."""
        manager.add_contact(sample_contact)

        another_contact = Contact(
            name="Jane Doe",
            email="jane@example.com",
            phone="987-654-3210"
        )
        manager.add_contact(another_contact)

        contacts = manager.get_all_contacts()
        assert len(contacts) == 2

    def test_persistence(self, temp_storage, sample_contact):
        """Test that contacts are persisted and loaded."""
        # Create manager and add contact
        manager1 = ContactManager(temp_storage)
        manager1.add_contact(sample_contact)

        # Create new manager with same storage
        manager2 = ContactManager(temp_storage)

        assert len(manager2.contacts) == 1
        assert manager2.contacts[0].name == "John Doe"

    def test_get_statistics(self, manager):
        """Test getting contact statistics."""
        contact1 = Contact(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890",
            address="123 Main St"
        )
        contact2 = Contact(
            name="Jane Doe",
            email="jane@example.com",
            phone="987-654-3210",
            notes="Important"
        )

        manager.add_contact(contact1)
        manager.add_contact(contact2)

        stats = manager.get_statistics()

        assert stats['total_contacts'] == 2
        assert stats['with_address'] == 1
        assert stats['with_notes'] == 1
