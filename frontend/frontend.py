"""
Frontend module for Restaurant Management System
This module contains all frontend logic and display functions
"""

import sys
from pathlib import Path

# Add parent directory to path to import backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel,
                              QPushButton, QVBoxLayout, QCheckBox ,QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

DARK_BG    = "#1a120b"
GOLD       = "#d4af37"
LIGHT_TEXT = "#f5e6c8"
INPUT_BG   = "#251a0f"

MAIN_STYLE = f"""
    QWidget {{
        background-color: {DARK_BG};
        color: {LIGHT_TEXT};
        font-family: 'Arial';
    }}
    QPushButton {{
        background-color: transparent;
        color: {GOLD};
        border: 1px solid {GOLD};
        padding: 10px 28px;
        font-size: 13px;
        letter-spacing: 2px;
        border-radius: 2px;
        min-width: 140px;
    }}
    QPushButton:hover {{
        background-color: rgba(212, 175, 55, 0.15);
        color: {LIGHT_TEXT};
    }}
    QPushButton:pressed {{
        background-color: rgba(212, 175, 55, 0.25);
    }}
    QLineEdit {{
        background-color: {INPUT_BG};
        border: none;
        border-bottom: 1px solid rgba(212, 175, 55, 0.4);
        color: {LIGHT_TEXT};
        font-size: 15px;
        padding: 8px 4px;
        border-radius: 0px;
    }}
    QLineEdit:focus {{
        border-bottom: 1px solid {GOLD};
    }}
    QLabel {{
        color: {LIGHT_TEXT};
        background-color: transparent;
        font-size: 14px;
    }}
    QCheckBox {{
        color: rgba(212,175,55,0.7);
        font-size: 12px;
        letter-spacing: 2px;
        spacing: 6px;
    }}
    QCheckBox::indicator {{
        width: 14px;
        height: 14px;
        border: 1px solid rgba(212,175,55,0.4);
        background: transparent;
        border-radius: 2px;
    }}
    QCheckBox::indicator:checked {{
        background-color: rgba(212,175,55,0.3);
        border-color: #d4af37;
    }}
"""

TITLE_LABEL_STYLE = f"color: {LIGHT_TEXT}; font-size: 28px; letter-spacing: 1px;"
SMALL_LABEL_STYLE = f"color: rgba(212,175,55,0.75); font-size: 11px; letter-spacing: 3px; text-transform: uppercase;"
BACK_BTN_STYLE = f"""
    QPushButton {{
        background: transparent;
        border: none;
        color: rgba(212,175,55,0.5);
        font-size: 12px;
        letter-spacing: 2px;
        padding: 6px;
        min-width: 0;
    }}
    QPushButton:hover {{ color: {GOLD}; }}
"""


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Management System")
        self.resize(900, 700)
        self.setStyleSheet(MAIN_STYLE)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background: transparent;")
        layout.addWidget(self.stack)

        self.choose_page   = self.create_choose_page()
        self.login_page = self.create_login_page()
        self.register_page = self.create_register_page()

        self.stack.addWidget(self.choose_page)
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)

    def create_choose_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(16)
        page.setLayout(layout)

        subtitle = QLabel("RESTAURANT MANAGEMENT")
        subtitle.setStyleSheet(SMALL_LABEL_STYLE)
        subtitle.setAlignment(Qt.AlignCenter)

        title = QLabel("მოგესალმებით")
        title.setFont(QFont("Arial", 30))
        title.setStyleSheet(TITLE_LABEL_STYLE)
        title.setAlignment(Qt.AlignCenter)

        ornament = QLabel("— ✦ —")
        ornament.setStyleSheet("color: rgba(212,175,55,0.5); font-size: 16px; letter-spacing: 8px;")
        ornament.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton("ავტორიზაცია")
        self.btn1.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        layout.addWidget(subtitle)
        layout.addWidget(title)
        layout.addWidget(ornament)
        layout.addSpacing(12)
        layout.addWidget(self.btn1, 0, Qt.AlignCenter)
        return page

    def create_login_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)
        page.setLayout(layout)

        subtitle = QLabel("AUTHORIZATION")
        subtitle.setStyleSheet(SMALL_LABEL_STYLE)
        subtitle.setAlignment(Qt.AlignCenter)

        title = QLabel("ავტორიზაცია")
        title.setFont(QFont("Georgia", 24))
        title.setStyleSheet(TITLE_LABEL_STYLE)
        title.setAlignment(Qt.AlignCenter)

        ornament = QLabel("— ✦ —")
        ornament.setStyleSheet("color: rgba(212,175,55,0.5); font-size: 16px; letter-spacing: 8px;")
        ornament.setAlignment(Qt.AlignCenter)

        # სახელის შეყვანა
        lbl_name = QLabel("სახელი / მეილი")
        lbl_name.setStyleSheet(SMALL_LABEL_STYLE)

        self.txt_name = QLineEdit()
        self.txt_name.setPlaceholderText("შეიყვანეთ სახელი, მეილი...")
        self.txt_name.setFixedWidth(340)

        # შეცდომის ტექსტი სახელისთვის (თავიდან ცარიელია)
        self.error_name = QLabel("")
        self.error_name.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.error_name.setFixedWidth(340)

        lbl_pass = QLabel("პაროლი")
        lbl_pass.setStyleSheet(SMALL_LABEL_STYLE)

        self.txt_pass = QLineEdit()
        self.txt_pass.setPlaceholderText("შეიყვანეთ პაროლი...")
        self.txt_pass.setEchoMode(QLineEdit.Password)
        self.txt_pass.setFixedWidth(340)

        # შეცდომის ტექსტი პაროლისთვის (თავიდან ცარიელია)
        self.error_pass = QLabel("")
        self.error_pass.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.error_pass.setFixedWidth(340)
        
        # პაროლის ჩვენება
        self.show_pass = QCheckBox("პაროლის ჩვენება")
        self.show_pass.stateChanged.connect(self.paroli)

        self.enter = QPushButton("შესვლა")
        self.enter.clicked.connect(self.check_login)  

        self.reg = QPushButton("რეგისტრაცია")
        self.reg.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        self.ukan = QPushButton("← უკან")
        self.ukan.setStyleSheet(BACK_BTN_STYLE)
        self.ukan.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(subtitle)
        layout.addWidget(title)
        layout.addWidget(ornament)
        layout.addSpacing(8)

        layout.addWidget(lbl_name, 0, Qt.AlignCenter)
        layout.addWidget(self.txt_name, 0, Qt.AlignCenter)
        layout.addWidget(self.error_name, 0, Qt.AlignCenter)

        layout.addSpacing(4)
        layout.addWidget(lbl_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.txt_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.error_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.show_pass, 0, Qt.AlignLeft)

        layout.addSpacing(12)
        layout.addWidget(self.enter, 0, Qt.AlignCenter)
        layout.addWidget(self.reg, 0, Qt.AlignCenter)
        layout.addWidget(self.ukan, 0, Qt.AlignCenter)

        return page

    def check_login(self):
        is_valid = True

        # სახელის შემოწმება
        if not self.txt_name.text().strip():
            # თუ ცარიელია, ხაზი წითლდება და იწერება ტექსტი
            self.txt_name.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.error_name.setText("შეიყვანეთ სახელი!")
            is_valid = False
        else:
            # თუ შევსებულია, უბრუნდება საწყის სტილს (ცარიელი სტრინგი აბრუნებს MAIN_STYLE-ის პარამეტრებს)
            self.txt_name.setStyleSheet("")
            self.error_name.setText("")

        # პაროლის შემოწმება
        if not self.txt_pass.text().strip():
            self.txt_pass.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.error_pass.setText("შეიყვანეთ პაროლი!")
            is_valid = False
        else:
            self.txt_pass.setStyleSheet("")
            self.error_pass.setText("")

        # თუ ორივე ველი წარმატებით შევსებულია
        if is_valid:
            print("მონაცემები სწორია! გადადის მთავარ მენიუში...")

    def paroli(self, state):
        if state == Qt.Checked:
            self.txt_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.txt_pass.setEchoMode(QLineEdit.Password)


    def create_register_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)
        page.setLayout(layout)

        subtitle = QLabel("REGISTER")
        subtitle.setStyleSheet(SMALL_LABEL_STYLE)
        subtitle.setAlignment(Qt.AlignCenter)

        title = QLabel("რეგისტრაცია")
        title.setFont(QFont("Arial", 24))
        title.setStyleSheet(TITLE_LABEL_STYLE)
        title.setAlignment(Qt.AlignCenter)

        ornament = QLabel("— ✦ —")
        ornament.setStyleSheet("color: rgba(212,175,55,0.5); font-size: 16px; letter-spacing: 8px;")
        ornament.setAlignment(Qt.AlignCenter)

        # რეგისტრაციის სახელი
        lbl_name = QLabel("სახელი:")
        lbl_name.setStyleSheet(SMALL_LABEL_STYLE)

        self.name = QLineEdit()
        self.name.setPlaceholderText("შეიყვანეთ სახელი...")
        self.name.setFixedWidth(340)

        # რეგისტრაციის მეილი
        lbl_email = QLabel("მეილი:")
        lbl_email.setStyleSheet(SMALL_LABEL_STYLE)

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("შეიყვანეთ მეილი...") 
        self.txt_email.setFixedWidth(340)

        # რეგისტრაციის ნომერი
        lbl_num = QLabel("ნომერი:")
        lbl_num.setStyleSheet(SMALL_LABEL_STYLE)

        self.txt_num = QLineEdit()
        self.txt_num.setPlaceholderText("შეიყვანეთ ნომერი...")
        self.txt_num.setFixedWidth(340)

        lbl_create_pass = QLabel("პაროლი:")
        lbl_create_pass.setStyleSheet(SMALL_LABEL_STYLE)

        self.txt_create_pass = QLineEdit()
        self.txt_create_pass.setPlaceholderText("შეიყვანეთ პაროლი...")
        self.txt_create_pass.setEchoMode(QLineEdit.Password)
        self.txt_create_pass.setFixedWidth(340)
        
        # პაროლის ჩვენება
        self.show_pass = QCheckBox("პაროლის ჩვენება")
        self.show_pass.stateChanged.connect(self.paroli1)

        self.button = QPushButton("რეგისტრაცია")
        # self.button.clicked.connect()

        layout.addWidget(subtitle)
        layout.addWidget(title)
        layout.addWidget(ornament)

        layout.addWidget(lbl_name, 0, Qt.AlignLeft)
        layout.addWidget(self.name, 0, Qt.AlignCenter)
        
        layout.addWidget(lbl_email, 0, Qt.AlignLeft)
        layout.addWidget(self.txt_email, 0, Qt.AlignCenter)

        layout.addWidget(lbl_num, 0, Qt.AlignLeft)
        layout.addWidget(self.txt_num, 0, Qt.AlignCenter)

        layout.addWidget(lbl_create_pass, 0, Qt.AlignLeft)
        layout.addWidget(self.txt_create_pass, 0, Qt.AlignCenter)

        layout.addWidget(self.show_pass, 0, Qt.AlignLeft)
        layout.addWidget(self.button, 0, Qt.AlignCenter)


        return page
    def paroli1(self, state):
        if state == Qt.Checked:
            self.txt_create_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.txt_create_pass.setEchoMode(QLineEdit.Password)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())