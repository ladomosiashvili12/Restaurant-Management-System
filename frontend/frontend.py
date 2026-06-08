"""
Frontend module for Restaurant Management System
This module contains all frontend logic and display functions
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.backend import customerR, get_menu, customerV, check_gift_card

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel,
                              QPushButton, QVBoxLayout, QHBoxLayout,
                              QCheckBox, QStackedWidget, QFrame, QDialog, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# ფერები
DARK_BG    = "#1a120b"
GOLD       = "#d4af37"
LIGHT_TEXT = "#f5e6c8"
INPUT_BG   = "#251a0f"
NAV_BG     = "#0f0a05"
HERO_BG    = "#2a1a0a"

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
SMALL_LABEL_STYLE = f"color: rgba(212,175,55,0.75); font-size: 11px; letter-spacing: 3px;"
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

class MenuWindow(QDialog):
    def __init__(self, login=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("მენიუ")
        self.resize(800, 600)
        self.setStyleSheet(f"background-color: {DARK_BG}; color: {LIGHT_TEXT};")
        
        layout = QVBoxLayout(self)
        
        title = QLabel("ჩვენი მენიუ")
        title.setFont(QFont("Georgia", 24))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        #მენიუს შინაარსი
        items, discount = get_menu(login)
        if discount:
            gift_label = QLabel("🎁 გილოცავთ!თქვენ გაქვთ 20%-იანი ფასდაკლება!")
            gift_label.setStyleSheet(f"color: {GOLD}; font-size: 14px;")
            gift_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(gift_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        container_layout = QVBoxLayout(container)

        for name, price in items:  # ← backend-იდან მოაქვს
            row = QHBoxLayout()
            row.addWidget(QLabel(name))
            row.addStretch()
            row.addWidget(QLabel(f"{price} ₾"))
            container_layout.addLayout(row)

        scroll.setWidget(container)
        layout.addWidget(scroll)

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Management System")
        self.resize(1000, 750)
        self.setStyleSheet(MAIN_STYLE)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background: transparent;")
        layout.addWidget(self.stack)

        self.choose_page   = self.create_choose_page()
        self.login_page    = self.create_login_page()
        self.register_page = self.create_register_page()
        self.main_page     = self.create_main_page()

        self.stack.addWidget(self.choose_page)    # index 0
        self.stack.addWidget(self.login_page)     # index 1
        self.stack.addWidget(self.register_page)  # index 2
        self.stack.addWidget(self.main_page)      # index 3

    
    # არჩევის გვერდი
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
    
    # 1 ავტორიზაციის გვერდი
     
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

        lbl_name = QLabel("სახელი / მეილი")
        lbl_name.setStyleSheet(SMALL_LABEL_STYLE)

        self.login_name = QLineEdit()
        self.login_name.setPlaceholderText("შეიყვანეთ სახელი, მეილი...")
        self.login_name.setFixedWidth(340)

        self.login_red_name = QLabel("")
        self.login_red_name.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.login_red_name.setFixedWidth(340)

        lbl_pass = QLabel("პაროლი")
        lbl_pass.setStyleSheet(SMALL_LABEL_STYLE)

        self.login_pass = QLineEdit()
        self.login_pass.setPlaceholderText("შეიყვანეთ პაროლი...")
        self.login_pass.setEchoMode(QLineEdit.Password)
        self.login_pass.setFixedWidth(340)

        self.login_red_pass = QLabel("")
        self.login_red_pass.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.login_red_pass.setFixedWidth(340)

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
        layout.addWidget(self.login_name, 0, Qt.AlignCenter)
        layout.addWidget(self.login_red_name, 0, Qt.AlignCenter)
        layout.addSpacing(4)
        layout.addWidget(lbl_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.login_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.login_red_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.show_pass, 0, Qt.AlignLeft)
        layout.addSpacing(12)
        layout.addWidget(self.enter, 0, Qt.AlignCenter)
        layout.addWidget(self.reg, 0, Qt.AlignCenter)
        layout.addWidget(self.ukan, 0, Qt.AlignCenter)
        return page

    def check_login(self):
        valid = True
        if not self.login_name.text().strip():
            self.login_name.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.login_red_name.setText("შეიყვანეთ სახელი!")
            valid = False
        else:
            self.login_name.setStyleSheet("")
            self.login_red_name.setText("")

        if not self.login_pass.text().strip():
            self.login_pass.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.login_red_pass.setText("შეიყვანეთ პაროლი!")
            valid = False
        else:
            self.login_pass.setStyleSheet("")
            self.login_red_pass.setText("")

        # ვალიდაცია — გადადი მთავარ გვერდზე
        if valid:
            login    = self.login_name.text().strip()
            password = self.login_pass.text().strip()
        
            customer = customerV(login, password)
            result   = customer.checkV()
        
            if "✅" in result:
                self.current_login = login
                self.stack.setCurrentIndex(3)  
            else:
                self.login_red_pass.setText(result)

    def paroli(self, state):
        if state == Qt.Checked:
            self.login_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.login_pass.setEchoMode(QLineEdit.Password)

    #  რეგისტრაციის გვერდი
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

        lbl_name = QLabel("სახელი:")
        lbl_name.setStyleSheet(SMALL_LABEL_STYLE)
        self.reg_name = QLineEdit()
        self.reg_name.setPlaceholderText("შეიყვანეთ სახელი...")
        self.reg_name.setFixedWidth(340)
        self.reg_red_name = QLabel("")
        self.reg_red_name.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.reg_red_name.setFixedWidth(340)

        lbl_email = QLabel("მეილი:")
        lbl_email.setStyleSheet(SMALL_LABEL_STYLE)
        self.reg_email = QLineEdit()
        self.reg_email.setPlaceholderText("შეიყვანეთ მეილი...")
        self.reg_email.setFixedWidth(340)
        self.reg_red_email = QLabel("")
        self.reg_red_email.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.reg_red_email.setFixedWidth(340)

        lbl_num = QLabel("ნომერი:")
        lbl_num.setStyleSheet(SMALL_LABEL_STYLE)
        self.reg_num = QLineEdit()
        self.reg_num.setPlaceholderText("შეიყვანეთ ნომერი...")
        self.reg_num.setFixedWidth(340)
        self.reg_red_num = QLabel("")
        self.reg_red_num.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.reg_red_num.setFixedWidth(340)

        lbl_pass = QLabel("პაროლი:")
        lbl_pass.setStyleSheet(SMALL_LABEL_STYLE)
        self.reg_pass = QLineEdit()
        self.reg_pass.setPlaceholderText("შეიყვანეთ პაროლი...")
        self.reg_pass.setEchoMode(QLineEdit.Password)
        self.reg_pass.setFixedWidth(340)
        self.reg_red_pass = QLabel("")
        self.reg_red_pass.setStyleSheet("color: #ff4d4d; font-size: 11px;")
        self.reg_red_pass.setFixedWidth(340)

        self.result = QLabel("")
        self.result.setStyleSheet("color: #ff4d4d; font-size: 11px")
        self.result.setFixedWidth(340)

        self.show_pass_reg = QCheckBox("პაროლის ჩვენება")
        self.show_pass_reg.stateChanged.connect(self.paroli1)

        self.button = QPushButton("რეგისტრაცია")
        self.button.clicked.connect(self.register_check)
        self.button.clicked.connect(self.register_user)

        ukan_reg = QPushButton("← უკან")
        ukan_reg.setStyleSheet(BACK_BTN_STYLE)
        ukan_reg.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        layout.addWidget(subtitle)
        layout.addWidget(title)
        layout.addWidget(ornament)

        layout.addWidget(lbl_name, 0, Qt.AlignLeft)
        layout.addWidget(self.reg_name, 0, Qt.AlignCenter)
        layout.addWidget(self.reg_red_name, 0, Qt.AlignLeft)
        
        layout.addWidget(lbl_email, 0, Qt.AlignLeft)
        layout.addWidget(self.reg_email, 0, Qt.AlignCenter)
        layout.addWidget(self.reg_red_email, 0, Qt.AlignLeft)
        
        layout.addWidget(lbl_num, 0, Qt.AlignLeft)
        layout.addWidget(self.reg_num, 0, Qt.AlignCenter)
        layout.addWidget(self.reg_red_num, 0, Qt.AlignLeft)
        
        layout.addWidget(lbl_pass, 0, Qt.AlignLeft)
        layout.addWidget(self.reg_pass, 0, Qt.AlignCenter)
        layout.addWidget(self.reg_red_pass, 0, Qt.AlignLeft)
        
        layout.addWidget(self.result, 0, Qt.AlignCenter)
        
        layout.addWidget(self.show_pass_reg, 0, Qt.AlignLeft)
        
        layout.addWidget(self.button, 0, Qt.AlignCenter)
        
        layout.addWidget(ukan_reg, 0, Qt.AlignCenter)
        return page

    def register_check(self):
        if not self.reg_name.text().strip():
            self.reg_name.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.reg_red_name.setText("შეიყვანეთ სახელი!")
        else:
            self.reg_name.setStyleSheet("")
            self.reg_red_name.setText("")

        if not self.reg_email.text().strip():
            self.reg_email.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.reg_red_email.setText("შეიყვანეთ მეილი!")
        else:
            self.reg_email.setStyleSheet("")
            self.reg_red_email.setText("")

        if not self.reg_num.text().strip():
            self.reg_num.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.reg_red_num.setText("შეიყვანეთ ნომერი!")
        else:
            self.reg_num.setStyleSheet("")
            self.reg_red_num.setText("")

        if not self.reg_pass.text().strip():
            self.reg_pass.setStyleSheet(f"border-bottom: 1px solid #ff4d4d; background-color: {INPUT_BG};")
            self.reg_red_pass.setText("შეიყვანეთ პაროლი!")
        else:
            self.reg_pass.setStyleSheet("")
            self.reg_red_pass.setText("")

    def paroli1(self, state):
        if state == Qt.Checked:
            self.reg_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.reg_pass.setEchoMode(QLineEdit.Password)

    def register_user(self):
        username = self.reg_name.text().strip()
        email    = self.reg_email.text().strip()
        phone    = self.reg_num.text().strip()
        password = self.reg_pass.text().strip()
        customer = customerR(username, phone, email, password)
        self.result.setText(customer.checkR())

    # მთავარი გვერდი
    def create_main_page(self):
        page = QWidget()
        page.setStyleSheet(f"background-color: {DARK_BG};")
        main_layout = QVBoxLayout(page)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        navbar = QWidget()
        navbar.setFixedHeight(52)
        navbar.setStyleSheet(f"background-color: {NAV_BG};")
        nav_layout = QHBoxLayout(navbar)
        nav_layout.setContentsMargins(30, 0, 30, 0)

        about_btn = self._nav_btn("ABOUT")
        # about_btn.clicked.connect(self.open_about)

        menu_btn = self._nav_btn("MENUS")
        menu_btn.clicked.connect(self.open_menu)



        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(menu_btn)

        nav_layout.addStretch()

        logo = QLabel("nammeee")
        logo.setFont(QFont("Georgia", 18))
        logo.setStyleSheet(f"color: {GOLD}; letter-spacing: 2px;")
        logo.setAlignment(Qt.AlignCenter)
        nav_layout.addWidget(logo)

        nav_layout.addStretch()

        right_links = ["GIFT CARD", "RESERVATIONS", "CONTACT US"]
        for text in right_links:
            nav_layout.addWidget(self._nav_btn(text))

        # გასვლის ღილაკი navbar-ში
        logout_btn = QPushButton("Log out")
        logout_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                border: none;
                color: rgba(212,175,55,0.5);
                font-size: 11px;
                letter-spacing: 2px;
                padding: 6px 10px;
                min-width: 0;
            }}
            QPushButton:hover {{ color: #ff4d4d; }}
        """)
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        nav_layout.addWidget(logout_btn)

        hero = QWidget()
        hero.setMinimumHeight(460)
        hero.setStyleSheet(f"""
            background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #1a0e05,
                stop:0.4 #2e1a08,
                stop:1 #1a0e05
            );
        """)
        hero_layout = QVBoxLayout(hero)
        hero_layout.setAlignment(Qt.AlignCenter)
        hero_layout.setSpacing(14)

        welcome = QLabel("WELCOME")
        welcome.setFont(QFont("Arial", 58, QFont.Bold))
        welcome.setStyleSheet(f"color: #ffffff; letter-spacing: 10px; background: transparent;")
        welcome.setAlignment(Qt.AlignCenter)

        sub = QLabel("ragacaa")
        sub.setFont(QFont("Georgia", 12))
        sub.setStyleSheet("color: rgba(255,255,255,180); background: transparent; letter-spacing: 1px;")
        sub.setAlignment(Qt.AlignCenter)

        # ოქროსფერი გამყოფი ხაზი
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFixedWidth(120)
        line.setStyleSheet(f"color: {GOLD}; background-color: {GOLD};")

        line_wrapper = QHBoxLayout()
        line_wrapper.addStretch()
        line_wrapper.addWidget(line)
        line_wrapper.addStretch()

        book_btn = QPushButton("BOOK A TABLE")
        book_btn.setFixedSize(190, 44)
        book_btn.setFont(QFont("Arial", 10, QFont.Bold))
        book_btn.setStyleSheet(f"""
            QPushButton {{
                color: #ffffff;
                background: transparent;
                border: 2px solid #ffffff;
                letter-spacing: 3px;
            }}
            QPushButton:hover {{
                background: rgba(255,255,255,25);
                border-color: {GOLD};
                color: {GOLD};
            }}
        """)
        book_btn.setCursor(Qt.PointingHandCursor)
        book_btn.clicked.connect

        btn_wrapper = QHBoxLayout()
        btn_wrapper.addStretch()
        btn_wrapper.addWidget(book_btn)
        btn_wrapper.addStretch()

        hero_layout.addStretch()
        hero_layout.addSpacing(10)
        hero_layout.addWidget(welcome)
        hero_layout.addWidget(sub)
        hero_layout.addSpacing(6)
        hero_layout.addLayout(line_wrapper)
        hero_layout.addSpacing(10)
        hero_layout.addLayout(btn_wrapper)
        hero_layout.addStretch()

        main_layout.addWidget(navbar)
        main_layout.addWidget(hero)

        return page

    def _nav_btn(self, text):
        btn = QPushButton(text)
        btn.setFlat(True)
        btn.setFont(QFont("Arial", 9, QFont.Bold))
        btn.setStyleSheet(f"""
            QPushButton {{
                color: #cccccc;
                background: transparent;
                border: none;
                padding: 6px 12px;
                letter-spacing: 1px;
                min-width: 0;
            }}
            QPushButton:hover {{ color: {GOLD}; }}
        """)
        btn.setCursor(Qt.PointingHandCursor)
        return btn
    
    def open_menu(self):
        self.menus_window = MenuWindow(login=self.current_login)
        self.menus_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())
