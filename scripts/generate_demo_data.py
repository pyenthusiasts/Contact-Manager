#!/usr/bin/env python3
"""
Generate demo contact data for testing Contact Manager.

This script creates a set of realistic demo contacts that can be used
for testing and demonstration purposes.
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from contact_manager.models import Contact
from contact_manager.manager import ContactManager


def generate_demo_contacts():
    """Generate a list of demo contacts."""
    demo_data = [
        {
            "name": "Alice Johnson",
            "email": "alice.johnson@techcorp.com",
            "phone": "+1-555-0101",
            "address": "123 Tech Street, San Francisco, CA 94102",
            "notes": "CTO at TechCorp, interested in AI solutions",
        },
        {
            "name": "Bob Smith",
            "email": "bob.smith@example.com",
            "phone": "(555) 234-5678",
            "address": "456 Main Ave, New York, NY 10001",
            "notes": "Marketing consultant, follow up quarterly",
        },
        {
            "name": "Carol Williams",
            "email": "carol.w@designstudio.io",
            "phone": "555-876-5432",
            "address": None,
            "notes": "Freelance designer, prefers email contact",
        },
        {
            "name": "David Brown",
            "email": "david.brown@startup.com",
            "phone": "+1 555 345 6789",
            "address": "789 Innovation Blvd, Austin, TX 78701",
            "notes": "Startup founder, available for collaboration",
        },
        {
            "name": "Emma Davis",
            "email": "emma.davis@consulting.com",
            "phone": "555.456.7890",
            "address": "321 Business Park, Boston, MA 02101",
            "notes": "Business consultant, monthly meetings scheduled",
        },
        {
            "name": "Frank Miller",
            "email": "frank.m@ventures.com",
            "phone": "+44 20 7123 4567",
            "address": "10 Finance Street, London, UK EC2M 7PP",
            "notes": "VC investor, interested in tech startups",
        },
        {
            "name": "Grace Lee",
            "email": "grace.lee@dataanalytics.com",
            "phone": "1234567890",
            "address": None,
            "notes": "Data scientist, Python enthusiast",
        },
        {
            "name": "Henry Taylor",
            "email": "h.taylor@lawfirm.com",
            "phone": "(555) 987-6543",
            "address": "555 Legal Ave, Chicago, IL 60601",
            "notes": "Corporate lawyer, handle all legal matters",
        },
        {
            "name": "Iris Chen",
            "email": "iris.chen@research.edu",
            "phone": "+1-555-111-2222",
            "address": "Research Lab, University Campus, Seattle, WA 98105",
            "notes": "Research scientist, collaborate on projects",
        },
        {
            "name": "Jack Wilson",
            "email": "jack.wilson@sales.biz",
            "phone": "555-333-4444",
            "address": "888 Commerce Dr, Miami, FL 33101",
            "notes": "Sales director, quarterly business review",
        },
    ]

    return [Contact(**data) for data in demo_data]


def main():
    """Main function to generate and save demo data."""
    print("Contact Manager - Demo Data Generator")
    print("=" * 50)

    # Ask for confirmation
    response = input("\nThis will add 10 demo contacts. Continue? (yes/no): ")

    if response.lower() not in ["yes", "y"]:
        print("Operation cancelled.")
        return

    # Get storage path
    storage_path = input("\nEnter storage path (default: data/contacts.json): ").strip()
    if not storage_path:
        storage_path = "data/contacts.json"

    try:
        # Create manager
        manager = ContactManager(storage_path)
        initial_count = len(manager.contacts)

        # Generate and add contacts
        demo_contacts = generate_demo_contacts()
        added_count = 0

        print(f"\nAdding demo contacts...")

        for contact in demo_contacts:
            try:
                manager.add_contact(contact)
                added_count += 1
                print(f"  ✓ Added: {contact.name}")
            except ValueError as e:
                print(f"  ✗ Skipped {contact.name}: {e}")

        print(f"\n{'=' * 50}")
        print(f"Successfully added {added_count} demo contacts!")
        print(f"Total contacts: {initial_count} → {len(manager.contacts)}")
        print(f"Data saved to: {storage_path}")
        print(f"{'=' * 50}\n")

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
