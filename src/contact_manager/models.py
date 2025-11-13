"""
Contact model definition.

This module defines the Contact class which represents a single contact
with validation capabilities.
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from .validation import validate_email, validate_phone


@dataclass
class Contact:
    """
    A class to represent a contact.

    Attributes
    ----------
    name : str
        The name of the contact.
    email : str
        The email address of the contact.
    phone : str
        The phone number of the contact.
    address : Optional[str]
        The physical address of the contact (optional).
    notes : Optional[str]
        Additional notes about the contact (optional).
    created_at : datetime
        The timestamp when the contact was created.
    updated_at : datetime
        The timestamp when the contact was last updated.
    """

    name: str
    email: str
    phone: str
    address: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate contact data after initialization."""
        self._validate()

    def _validate(self):
        """Validate all contact fields."""
        if not self.name or not self.name.strip():
            raise ValueError("Name cannot be empty")

        if not validate_email(self.email):
            raise ValueError(f"Invalid email address: {self.email}")

        if not validate_phone(self.phone):
            raise ValueError(f"Invalid phone number: {self.phone}")

    def update(self, **kwargs):
        """
        Update contact fields.

        Parameters
        ----------
        **kwargs : dict
            Fields to update (name, email, phone, address, notes).
        """
        for key, value in kwargs.items():
            if hasattr(self, key) and key not in ['created_at']:
                setattr(self, key, value)

        self.updated_at = datetime.now()
        self._validate()

    def to_dict(self) -> dict:
        """Convert contact to dictionary format."""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Contact':
        """Create a Contact instance from a dictionary."""
        contact_data = data.copy()
        if 'created_at' in contact_data:
            contact_data['created_at'] = datetime.fromisoformat(contact_data['created_at'])
        if 'updated_at' in contact_data:
            contact_data['updated_at'] = datetime.fromisoformat(contact_data['updated_at'])
        return cls(**contact_data)

    def __str__(self) -> str:
        """Return string representation of contact."""
        result = f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
        if self.address:
            result += f", Address: {self.address}"
        if self.notes:
            result += f", Notes: {self.notes}"
        return result

    def __repr__(self) -> str:
        """Return detailed representation of contact."""
        return (f"Contact(name='{self.name}', email='{self.email}', "
                f"phone='{self.phone}', address='{self.address}', "
                f"notes='{self.notes}')")
