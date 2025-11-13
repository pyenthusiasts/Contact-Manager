"""
Contact Manager class for managing contact operations.

This module provides the ContactManager class which handles all
contact-related operations including CRUD operations and search.
"""

from typing import List, Optional
from .models import Contact
from .storage import ContactStorage


class ContactManager:
    """
    A class to manage contacts with persistence.

    Attributes
    ----------
    contacts : List[Contact]
        A list to store all contacts.
    storage : ContactStorage
        Storage handler for persisting contacts.
    """

    def __init__(self, storage_path: str = "data/contacts.json"):
        """
        Initialize the ContactManager.

        Parameters
        ----------
        storage_path : str
            Path to the storage file.
        """
        self.contacts: List[Contact] = []
        self.storage = ContactStorage(storage_path)
        self.load_contacts()

    def add_contact(self, contact: Contact) -> None:
        """
        Add a new contact to the list.

        Parameters
        ----------
        contact : Contact
            The contact to add.

        Raises
        ------
        ValueError
            If a contact with the same email already exists.
        """
        # Check for duplicate email
        if any(c.email.lower() == contact.email.lower() for c in self.contacts):
            raise ValueError(f"Contact with email '{contact.email}' already exists")

        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{contact.name}' added successfully!")

    def search_contact(self, query: str) -> List[Contact]:
        """
        Search for contacts by name, email, or phone.

        Parameters
        ----------
        query : str
            The search query (case-insensitive).

        Returns
        -------
        List[Contact]
            List of matching contacts.
        """
        query = query.lower()
        results = []

        for contact in self.contacts:
            if (query in contact.name.lower() or
                query in contact.email.lower() or
                query in contact.phone):
                results.append(contact)

        return results

    def get_contact_by_email(self, email: str) -> Optional[Contact]:
        """
        Get a contact by exact email match.

        Parameters
        ----------
        email : str
            The email address to search for.

        Returns
        -------
        Optional[Contact]
            The contact if found, None otherwise.
        """
        for contact in self.contacts:
            if contact.email.lower() == email.lower():
                return contact
        return None

    def update_contact(self, email: str, **kwargs) -> bool:
        """
        Update a contact's information.

        Parameters
        ----------
        email : str
            Email of the contact to update.
        **kwargs : dict
            Fields to update.

        Returns
        -------
        bool
            True if contact was updated, False if not found.

        Raises
        ------
        ValueError
            If the update would create invalid data.
        """
        contact = self.get_contact_by_email(email)
        if contact:
            contact.update(**kwargs)
            self.save_contacts()
            print(f"Contact '{contact.name}' updated successfully!")
            return True
        return False

    def delete_contact(self, email: str) -> bool:
        """
        Delete a contact by email.

        Parameters
        ----------
        email : str
            Email of the contact to delete.

        Returns
        -------
        bool
            True if contact was deleted, False if not found.
        """
        contact = self.get_contact_by_email(email)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            print(f"Contact '{contact.name}' deleted successfully!")
            return True
        return False

    def display_contacts(self) -> None:
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print(f"\n{'='*80}")
            print(f"Contacts List ({len(self.contacts)} total)")
            print(f"{'='*80}")
            for i, contact in enumerate(self.contacts, 1):
                print(f"\n{i}. {contact}")
            print(f"\n{'='*80}\n")

    def get_all_contacts(self) -> List[Contact]:
        """
        Get all contacts.

        Returns
        -------
        List[Contact]
            List of all contacts.
        """
        return self.contacts.copy()

    def save_contacts(self) -> None:
        """Save contacts to storage."""
        try:
            self.storage.save_contacts(self.contacts)
        except IOError as e:
            print(f"Error saving contacts: {e}")

    def load_contacts(self) -> None:
        """Load contacts from storage."""
        try:
            self.contacts = self.storage.load_contacts()
        except IOError as e:
            print(f"Error loading contacts: {e}")
            self.contacts = []

    def export_contacts(self, export_path: str) -> None:
        """
        Export contacts to a file.

        Parameters
        ----------
        export_path : str
            Path to the export file (supports .json and .csv).

        Raises
        ------
        IOError
            If there's an error exporting contacts.
        """
        try:
            self.storage.export_contacts(self.contacts, export_path)
            print(f"Contacts exported successfully to '{export_path}'!")
        except (IOError, ValueError) as e:
            print(f"Error exporting contacts: {e}")

    def get_statistics(self) -> dict:
        """
        Get statistics about the contacts.

        Returns
        -------
        dict
            Dictionary containing statistics.
        """
        return {
            'total_contacts': len(self.contacts),
            'with_address': sum(1 for c in self.contacts if c.address),
            'with_notes': sum(1 for c in self.contacts if c.notes)
        }
