from PyQt6.QtGui import QIntValidator, QIcon
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QGridLayout, QMessageBox)
from PyQt6.QtCore import Qt
import sys
import random
import string


class MainWindow(QMainWindow):
    """
    MainWindow class for the creation of the application
    """

    def __init__(self):
        """MainWindow constructor for the layout of the application"""
        super().__init__()

        # Set up window properties
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setMinimumSize(380, 220)

        # Set central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()

        # Password length input field
        pass_length = QLabel("Password Length:")
        self.pass_edit = QLineEdit()
        self.pass_edit.setValidator(QIntValidator(0, 300))  # Only allow integers in a valid range
        layout.addWidget(pass_length, 0, 0)
        layout.addWidget(self.pass_edit, 0, 1)

        # Number count input field
        num_count = QLabel("Amount of Numbers:")
        self.num_edit = QLineEdit()
        self.num_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(num_count, 1, 0)
        layout.addWidget(self.num_edit, 1, 1)

        # Special character count input field
        special_count = QLabel("Amount of Special Characters:")
        self.special_edit = QLineEdit()
        self.special_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(special_count, 2, 0)
        layout.addWidget(self.special_edit, 2, 1)

        # Alphabet count input field
        char_count = QLabel("Amount of Alphabets:")
        self.char_edit = QLineEdit()
        self.char_edit.setValidator(QIntValidator(0, 300))
        layout.addWidget(char_count, 3, 0)
        layout.addWidget(self.char_edit, 3, 1)

        # Button to generate password
        submit_button = QPushButton('Generate')
        layout.addWidget(submit_button, 4, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        submit_button.clicked.connect(self.generate_password)

        # Label to display generated password
        self.result = QLabel("")
        layout.addWidget(self.result, 5, 0, 1, 2)
        self.result.setStyleSheet("font-size: 16px; font-weight: bold; padding-left: 10px;")

        # Button to copy password to clipboard
        self.copy_button = QPushButton("Copy to Clipboard")
        layout.addWidget(self.copy_button, 6, 0, 2, 2, Qt.AlignmentFlag.AlignCenter)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setVisible(False)  # Hidden initially, shown after password generation

        # Button to clear fields
        clear_button = QPushButton("Clear")
        layout.addWidget(clear_button, 4, 1, 1, 2, Qt.AlignmentFlag.AlignCenter)
        clear_button.clicked.connect(self.clear_fields)  # Connect clear button to clear_fields method

        # Apply layout to the central widget and adjust window size
        central_widget.setLayout(layout)
        self.resize(400, 200)

    def generate_password(self):
        """Generate a password based on the user-specified length and character counts."""
        try:
            # Retrieve and validate user input
            pass_len = int(self.pass_edit.text())
            n_count = int(self.num_edit.text())
            s_count = int(self.special_edit.text())
            c_count = int(self.char_edit.text())
        except ValueError:
            # Show warning if any field is empty or contains invalid input
            QMessageBox.warning(self, "Input Error", "Please fill every field with a valid integer.")
            return

        # Ensure total specified character count doesn't exceed password length
        total_count = n_count + s_count + c_count
        if total_count > pass_len:
            QMessageBox.warning(self, "Input Error", "Total character count exceeds password length.")
            return

        # Generate each specified component of the password
        numbers = [str(random.randint(0, 9)) for _ in range(n_count)]
        special_chars = [random.choice(string.punctuation) for _ in range(s_count)]
        letters = [random.choice(string.ascii_letters) for _ in range(c_count)]

        # Fill remaining length with random letters, if necessary
        remaining_count = pass_len - total_count
        letters += [random.choice(string.ascii_letters) for _ in range(remaining_count)]

        # Combine all components, shuffle them, and display the generated password
        password_list = numbers + special_chars + letters
        random.shuffle(password_list)
        self.result.setText("".join(password_list))
        self.copy_button.setVisible(True)  # Show copy button after password is generated

    def copy_to_clipboard(self):
        """Copy the generated password to the system clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result.text())
        QMessageBox.information(self, "Copied", "Password copied to clipboard!")

    def clear_fields(self):
        """Clear all input fields and reset the displayed password."""
        self.pass_edit.clear()
        self.num_edit.clear()
        self.special_edit.clear()
        self.char_edit.clear()
        self.result.clear()
        self.copy_button.setVisible(False)  # Hide copy button after fields are cleared


if __name__ == '__main__':
    # Initialize the application and display the main window
    app = QApplication(sys.argv)
    app.setStyleSheet("font-family: Arial; font-size: 12pt;")
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
