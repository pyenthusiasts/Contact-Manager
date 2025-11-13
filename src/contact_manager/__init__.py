"""
Contact Manager - A simple contact management system.

This package provides a simple and intuitive way to manage contacts
with features like adding, searching, updating, deleting, and exporting contacts.
"""

__version__ = "2.0.0"
__author__ = "Contact Manager Team"

from .models import Contact
from .manager import ContactManager

__all__ = ["Contact", "ContactManager"]
