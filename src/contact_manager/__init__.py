"""
Contact Manager - A simple contact management system.

This package provides a simple and intuitive way to manage contacts
with features like adding, searching, updating, deleting, and exporting contacts.
"""

__version__ = "2.0.0"
__author__ = "Contact Manager Team"

from .logger import get_logger, setup_logger
from .manager import ContactManager
from .models import Contact

__all__ = ["Contact", "ContactManager", "get_logger", "setup_logger"]
