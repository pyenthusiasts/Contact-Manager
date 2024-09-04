class Contact:
    """
    A class to represent a contact.

    Attributes:
    -----------
    name : str
        The name of the contact.
    email : str
        The email address of the contact.
    phone : str
        The phone number of the contact.
    """

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class ContactManager:
    """
    A class to manage contacts.

    Attributes:
    -----------
    contacts : list
        A list to store all contacts.
    """

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact to the list."""
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def search_contact(self, name):
        """Searches for a contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contacts(self):
        """Displays all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts List:")
            for contact in self.contacts:
                print(contact)


def main():
    """Main function to interact with the contact manager."""
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            new_contact = Contact(name, email, phone)
            manager.add_contact(new_contact)

        elif choice == '2':
            name = input("Enter the name to search: ")
            result = manager.search_contact(name)
            if result:
                print("Contact Found:", result)
            else:
                print("Contact not found.")

        elif choice == '3':
            manager.display_contacts()

        elif choice == '4':
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

