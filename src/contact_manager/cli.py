"""
Command-line interface with argument parsing.

This module provides a CLI interface using argparse for advanced usage.
"""

import argparse
import sys
from pathlib import Path

from .logger import setup_logger
from .manager import ContactManager
from .models import Contact
from .ui import ContactManagerUI


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        prog="contact-manager",
        description="Contact Manager - A professional contact management system",
        epilog="For interactive mode, run without arguments.",
    )

    parser.add_argument(
        "--version", action="version", version="Contact Manager 2.0.0"
    )

    parser.add_argument(
        "--storage",
        type=str,
        default="data/contacts.json",
        help="Path to contacts storage file (default: data/contacts.json)",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Set logging level (default: WARNING)",
    )

    parser.add_argument(
        "--log-file", type=str, help="Path to log file (default: no file logging)"
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Interactive mode (default)
    subparsers.add_parser("interactive", help="Launch interactive mode")

    # Add contact
    add_parser = subparsers.add_parser("add", help="Add a new contact")
    add_parser.add_argument("name", type=str, help="Contact name")
    add_parser.add_argument("email", type=str, help="Contact email")
    add_parser.add_argument("phone", type=str, help="Contact phone")
    add_parser.add_argument("--address", type=str, help="Contact address")
    add_parser.add_argument("--notes", type=str, help="Contact notes")

    # Search contacts
    search_parser = subparsers.add_parser("search", help="Search for contacts")
    search_parser.add_argument("query", type=str, help="Search query")

    # List all contacts
    subparsers.add_parser("list", help="List all contacts")

    # Delete contact
    delete_parser = subparsers.add_parser("delete", help="Delete a contact")
    delete_parser.add_argument("email", type=str, help="Email of contact to delete")
    delete_parser.add_argument(
        "--force", action="store_true", help="Skip confirmation prompt"
    )

    # Export contacts
    export_parser = subparsers.add_parser("export", help="Export contacts")
    export_parser.add_argument(
        "output", type=str, help="Output file path (.json or .csv)"
    )

    # Statistics
    subparsers.add_parser("stats", help="Show contact statistics")

    return parser


def handle_add_command(args, manager: ContactManager) -> int:
    """Handle add command."""
    try:
        contact = Contact(
            name=args.name,
            email=args.email,
            phone=args.phone,
            address=args.address,
            notes=args.notes,
        )
        manager.add_contact(contact)
        return 0
    except (ValueError, Exception) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_search_command(args, manager: ContactManager) -> int:
    """Handle search command."""
    results = manager.search_contact(args.query)

    if results:
        print(f"\nFound {len(results)} contact(s):\n")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact}")
        print()
        return 0
    else:
        print("No contacts found.")
        return 1


def handle_list_command(args, manager: ContactManager) -> int:
    """Handle list command."""
    manager.display_contacts()
    return 0


def handle_delete_command(args, manager: ContactManager) -> int:
    """Handle delete command."""
    contact = manager.get_contact_by_email(args.email)

    if not contact:
        print(f"No contact found with email '{args.email}'", file=sys.stderr)
        return 1

    if not args.force:
        print(f"Contact to delete: {contact}")
        response = input("Are you sure? (yes/no): ")
        if response.lower() not in ["yes", "y"]:
            print("Deletion cancelled.")
            return 0

    if manager.delete_contact(args.email):
        return 0
    else:
        return 1


def handle_export_command(args, manager: ContactManager) -> int:
    """Handle export command."""
    try:
        manager.export_contacts(args.output)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_stats_command(args, manager: ContactManager) -> int:
    """Handle stats command."""
    stats = manager.get_statistics()

    print("\n" + "=" * 50)
    print("Contact Statistics")
    print("=" * 50)
    print(f"Total Contacts: {stats['total_contacts']}")
    print(f"Contacts with Address: {stats['with_address']}")
    print(f"Contacts with Notes: {stats['with_notes']}")
    print("=" * 50 + "\n")

    return 0


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Setup logging
    setup_logger(
        level=args.log_level, log_file=args.log_file, console=(args.log_level != "CRITICAL")
    )

    # If no command specified, launch interactive mode
    if not args.command:
        ui = ContactManagerUI(args.storage)
        ui.run()
        return 0

    # Handle commands
    if args.command == "interactive":
        ui = ContactManagerUI(args.storage)
        ui.run()
        return 0

    # For non-interactive commands, create manager
    manager = ContactManager(args.storage)

    command_handlers = {
        "add": handle_add_command,
        "search": handle_search_command,
        "list": handle_list_command,
        "delete": handle_delete_command,
        "export": handle_export_command,
        "stats": handle_stats_command,
    }

    handler = command_handlers.get(args.command)
    if handler:
        return handler(args, manager)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
