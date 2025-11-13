#!/usr/bin/env python3
"""
Convenience script to run the Contact Manager application.

This script can be used to run the application directly without installation.
"""

import sys
from pathlib import Path

# Add src to path to allow imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from contact_manager.ui import main

if __name__ == "__main__":
    main()
