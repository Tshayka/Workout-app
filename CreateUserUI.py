import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QLabel,
                             QComboBox, QApplication)

class CreateUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(320, 240, 280, 220)
        self.setWindowTitle("Add new user")
        self.init_ui()


    def init_ui(self):

        # First line to add user name
        self.user_name_textbox = QLineEdit(self)
        self.user_name_textbox.move(10, 10)
        self.user_name_textbox.resize(190, 30)

        self.user_label = QLabel('Name', self)
        self.user_label.move(215, 10)
        self.user_label.resize(60, 30)

        self.weight_textbox = QLineEdit(self)
        self.weight_textbox.move(10, 50)
        self.weight_textbox.resize(50, 30)

        self.weight_type = QComboBox(self)
        self.weight_type.addItem("kg")
        self.weight_type.addItem("lb")
        self.weight_type.move(70, 50)
        self.weight_type.resize(60, 30)

        self.weight_label = QLabel('Weight', self)
        self.weight_label.move(215, 50)
        self.weight_label.resize(60, 30)

        # Form buttons for cancel and create
        self.user_cancel_button = QPushButton('Cancel', self)
        self.user_cancel_button.move(200, 180)
        self.user_cancel_button.resize(75, 30)
        self.user_cancel_button.clicked.connect(self.close)

        self.user_create_button = QPushButton('Create', self)
        self.user_create_button.move(120, 180)
        self.user_create_button.resize(75, 30)
        self.user_create_button.clicked.connect(self.create_user_file)
        self.user_create_button.clicked.connect(self.close)

        self.show()

    def add_user_name(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.name_add_button.setText(str(text))

    # Save file onto hard drive
    def create_user_file(self):

        name_area = str(self.user_name_textbox.text())
        weight_area = str(self.weight_textbox.text())
        weight_type = str(self.weight_type.currentText())

        save_name = name_area + ".txt"
        file_path = os.path.join("users", save_name)
        self.user_file = open(file_path, "w")
        self.user_file.write("Name of the user is %s,\n" % name_area)
        self.user_file.write("User weight is %s %s\n" % (weight_area, weight_type))
        self.user_file.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    workout = CreateUser()
    sys.exit(app.exec_())