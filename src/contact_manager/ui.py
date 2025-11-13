"""
User interface module for the Contact Manager.

This module provides an interactive command-line interface
for managing contacts.
"""

from typing import Optional
from .models import Contact
from .manager import ContactManager
from .validation import sanitize_input


class ContactManagerUI:
    """
    User interface for the Contact Manager application.

    Attributes
    ----------
    manager : ContactManager
        The contact manager instance.
    """

    def __init__(self, storage_path: str = "data/contacts.json"):
        """
        Initialize the UI.

        Parameters
        ----------
        storage_path : str
            Path to the storage file.
        """
        self.manager = ContactManager(storage_path)

    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*50)
        print("         CONTACT MANAGER v2.0")
        print("="*50)
        print("1.  Add New Contact")
        print("2.  Search Contacts")
        print("3.  Display All Contacts")
        print("4.  Update Contact")
        print("5.  Delete Contact")
        print("6.  Export Contacts")
        print("7.  View Statistics")
        print("8.  Exit")
        print("="*50)

    def get_input(self, prompt: str, required: bool = True) -> Optional[str]:
        """
        Get user input with validation.

        Parameters
        ----------
        prompt : str
            The prompt to display.
        required : bool
            Whether the input is required.

        Returns
        -------
        Optional[str]
            The sanitized input or None.
        """
        while True:
            value = input(prompt)
            value = sanitize_input(value)

            if value or not required:
                return value

            print("This field is required. Please enter a value.")

    def add_contact(self) -> None:
        """Add a new contact through user input."""
        print("\n--- Add New Contact ---")

        try:
            name = self.get_input("Enter name: ")
            email = self.get_input("Enter email: ")
            phone = self.get_input("Enter phone number: ")
            address = self.get_input("Enter address (optional): ", required=False)
            notes = self.get_input("Enter notes (optional): ", required=False)

            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                address=address,
                notes=notes
            )

            self.manager.add_contact(contact)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def search_contacts(self) -> None:
        """Search for contacts."""
        print("\n--- Search Contacts ---")

        query = self.get_input("Enter search query (name/email/phone): ")
        results = self.manager.search_contact(query)

        if results:
            print(f"\nFound {len(results)} contact(s):")
            print("-" * 80)
            for i, contact in enumerate(results, 1):
                print(f"{i}. {contact}")
            print("-" * 80)
        else:
            print("No contacts found matching your query.")

    def update_contact(self) -> None:
        """Update an existing contact."""
        print("\n--- Update Contact ---")

        email = self.get_input("Enter email of contact to update: ")
        contact = self.manager.get_contact_by_email(email)

        if not contact:
            print(f"No contact found with email '{email}'.")
            return

        print(f"\nCurrent details: {contact}")
        print("\nEnter new values (press Enter to keep current value):")

        updates = {}

        name = self.get_input(f"Name [{contact.name}]: ", required=False)
        if name:
            updates['name'] = name

        new_email = self.get_input(f"Email [{contact.email}]: ", required=False)
        if new_email:
            updates['email'] = new_email

        phone = self.get_input(f"Phone [{contact.phone}]: ", required=False)
        if phone:
            updates['phone'] = phone

        address = self.get_input(
            f"Address [{contact.address or 'None'}]: ",
            required=False
        )
        if address:
            updates['address'] = address

        notes = self.get_input(
            f"Notes [{contact.notes or 'None'}]: ",
            required=False
        )
        if notes:
            updates['notes'] = notes

        if updates:
            try:
                self.manager.update_contact(email, **updates)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_contact(self) -> None:
        """Delete a contact."""
        print("\n--- Delete Contact ---")

        email = self.get_input("Enter email of contact to delete: ")
        contact = self.manager.get_contact_by_email(email)

        if not contact:
            print(f"No contact found with email '{email}'.")
            return

        print(f"\nContact to delete: {contact}")
        confirm = self.get_input("Are you sure? (yes/no): ")

        if confirm.lower() in ['yes', 'y']:
            self.manager.delete_contact(email)
        else:
            print("Deletion cancelled.")

    def export_contacts(self) -> None:
        """Export contacts to a file."""
        print("\n--- Export Contacts ---")
        print("Supported formats: JSON (.json), CSV (.csv)")

        export_path = self.get_input("Enter export file path: ")

        if not (export_path.endswith('.json') or export_path.endswith('.csv')):
            print("Error: File must have .json or .csv extension.")
            return

        try:
            self.manager.export_contacts(export_path)
        except Exception as e:
            print(f"Error: {e}")

    def view_statistics(self) -> None:
        """Display contact statistics."""
        print("\n--- Contact Statistics ---")

        stats = self.manager.get_statistics()

        print(f"Total Contacts: {stats['total_contacts']}")
        print(f"Contacts with Address: {stats['with_address']}")
        print(f"Contacts with Notes: {stats['with_notes']}")

    def run(self) -> None:
        """Run the main application loop."""
        print("\nWelcome to Contact Manager!")

        if self.manager.contacts:
            print(f"Loaded {len(self.manager.contacts)} existing contact(s).")

        while True:
            try:
                self.display_menu()
                choice = input("\nEnter your choice (1-8): ").strip()

                if choice == '1':
                    self.add_contact()
                elif choice == '2':
                    self.search_contacts()
                elif choice == '3':
                    self.manager.display_contacts()
                elif choice == '4':
                    self.update_contact()
                elif choice == '5':
                    self.delete_contact()
                elif choice == '6':
                    self.export_contacts()
                elif choice == '7':
                    self.view_statistics()
                elif choice == '8':
                    print("\nThank you for using Contact Manager. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 8.")

            except KeyboardInterrupt:
                print("\n\nExiting Contact Manager. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def main():
    """Entry point for the application."""
    ui = ContactManagerUI()
    ui.run()


if __name__ == "__main__":
    main()
