"""
Frontend module for Restaurant Management System
This module contains all frontend logic and display functions
"""

import sys
from pathlib import Path

# Add parent directory to path to import backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.backend import say_hello

say_hello("lado")