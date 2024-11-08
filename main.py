from PyQt6.QtGui import QIntValidator, QIcon
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout,
                             QMessageBox)
from PyQt6.QtCore import Qt
import sys
import random
import string

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setMinimumSize(400, 150)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout()

        pass_length = QLabel("Password Length:")
        self.pass_edit = QLineEdit()
        self.pass_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(pass_length, 0, 0)
        layout.addWidget(self.pass_edit, 0, 1)

        num_count = QLabel("Amount of Numbers:")
        self.num_edit = QLineEdit()
        self.num_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(num_count, 1, 0)
        layout.addWidget(self.num_edit, 1, 1)

        special_count = QLabel("Amount of Special Characters:")
        self.special_edit = QLineEdit()
        self.special_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(special_count, 2, 0)
        layout.addWidget(self.special_edit, 2, 1)

        char_count = QLabel("Amount of Alphabets:")
        self.char_edit = QLineEdit()
        self.char_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(char_count, 3, 0)
        layout.addWidget(self.char_edit, 3, 1)

        submit_button = QPushButton('Submit')
        layout.addWidget(submit_button, 4, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        submit_button.clicked.connect(self.generate_password)

        self.result = QLabel("")
        layout.addWidget(self.result, 5, 0, 1, 2)
        self.result.setStyleSheet("font-size: 16px; font-weight: bold")

        central_widget.setLayout(layout)
        self.resize(400, 200)
        self.setCentralWidget(central_widget)

    def generate_password(self):
        try:
            pass_len = int(self.pass_edit.text())
            n_count = int(self.num_edit.text())
            s_count = int(self.special_edit.text())
            c_count = int(self.char_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please fill every column")
            return

        total_count = n_count + s_count + c_count
        if total_count > pass_len:
            QMessageBox.warning(self, "Input Error", "Total length exceeds password length.")
            return

        numbers = [str(random.randint(1, 9)) for _ in range(n_count)]
        special_chars = [random.choice(string.punctuation) for _ in range(s_count)]
        letters = [random.choice(string.ascii_letters) for _ in range(c_count)]

        remaining_count = pass_len - total_count
        letters += [random.choice(string.ascii_letters) for _ in range(remaining_count)]

        password_list = numbers + special_chars + letters
        random.shuffle(password_list)

        self.result.setText("".join(password_list))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("font-family: Arial; font-size: 12pt;")
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
