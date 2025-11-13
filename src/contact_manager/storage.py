"""
Data persistence layer for contacts.

This module handles saving and loading contacts to/from JSON files.
"""

import json
import os
from typing import List
from pathlib import Path
from .models import Contact


class ContactStorage:
    """
    Handles data persistence for contacts.

    Attributes
    ----------
    storage_path : Path
        The path to the JSON file where contacts are stored.
    """

    def __init__(self, storage_path: str = "data/contacts.json"):
        """
        Initialize the storage handler.

        Parameters
        ----------
        storage_path : str
            Path to the JSON file for storing contacts.
        """
        self.storage_path = Path(storage_path)
        self._ensure_storage_directory()

    def _ensure_storage_directory(self):
        """Ensure the storage directory exists."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def save_contacts(self, contacts: List[Contact]) -> None:
        """
        Save contacts to the storage file.

        Parameters
        ----------
        contacts : List[Contact]
            List of contacts to save.

        Raises
        ------
        IOError
            If there's an error writing to the file.
        """
        try:
            data = [contact.to_dict() for contact in contacts]
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise IOError(f"Failed to save contacts: {e}")

    def load_contacts(self) -> List[Contact]:
        """
        Load contacts from the storage file.

        Returns
        -------
        List[Contact]
            List of contacts loaded from storage.

        Raises
        ------
        IOError
            If there's an error reading from the file.
        """
        if not self.storage_path.exists():
            return []

        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Contact.from_dict(item) for item in data]
        except json.JSONDecodeError as e:
            raise IOError(f"Failed to parse contacts file: {e}")
        except Exception as e:
            raise IOError(f"Failed to load contacts: {e}")

    def export_contacts(self, contacts: List[Contact], export_path: str) -> None:
        """
        Export contacts to a specified file.

        Parameters
        ----------
        contacts : List[Contact]
            List of contacts to export.
        export_path : str
            Path to the export file.

        Raises
        ------
        IOError
            If there's an error writing to the file.
        """
        export_file = Path(export_path)
        export_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            if export_file.suffix.lower() == '.json':
                data = [contact.to_dict() for contact in contacts]
                with open(export_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            elif export_file.suffix.lower() == '.csv':
                import csv
                with open(export_file, 'w', newline='', encoding='utf-8') as f:
                    if contacts:
                        fieldnames = ['name', 'email', 'phone', 'address', 'notes']
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        for contact in contacts:
                            row = {
                                'name': contact.name,
                                'email': contact.email,
                                'phone': contact.phone,
                                'address': contact.address or '',
                                'notes': contact.notes or ''
                            }
                            writer.writerow(row)
            else:
                raise ValueError(f"Unsupported export format: {export_file.suffix}")
        except Exception as e:
            raise IOError(f"Failed to export contacts: {e}")
