"""
Frontend module for Restaurant Management System
This module contains all frontend logic and display functions
"""

import sys
# from pathlib import Path

# # Add parent directory to path to import backend
# sys.path.insert(0, str(Path(__file__).parent.parent))

# from backend.backend import say_hello

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class customer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restourant-Management_System")
        self.resize(700,900)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = customer()
    window.show()
    sys.exit(app.exec_())

print("gioio")