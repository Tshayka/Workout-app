import sys
import os
from PyQt5.QtWidgets import (QPushButton, QLabel, QApplication, QComboBox, QDialog, QMessageBox)
from PyQt5.QtGui import QIcon, QPixmap


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 640, 640)
        self.setWindowTitle("Extreme Workout")
        self.setWindowIcon(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'))
        self.user_list = ["None"]
        self.init_ui()
        self.reload_user_list()
        self.chosen_user = self.dropdown.currentText()

    def init_ui(self):
        pixmap = QPixmap(os.getcwd() + '\graphics' + '\workout_logo_2.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        # "Start session" button
        btn = QPushButton("Start \n session", self)
        btn.clicked.connect(self.init_main_UI)
        btn.resize(70, 70)
        btn.move(300, 370)
        btn.setStyleSheet(
            'QPushButton {background-color: #ffffff; color: #2E2E2E; font: bold 14px; border-radius: 5px;}')

        # "Add new" button
        btn = QPushButton("Add new", self)
        btn.clicked.connect(self.new_user)
        btn.resize(80, 30)
        btn.move(380, 370)
        btn.setStyleSheet('QPushButton {background-color: #ffffff; color: #2E2E2E; font: bold 14px; border-radius: 5px;}')

        # "Refresh" button
        refresh_btn = QPushButton("R", self)
        refresh_btn.clicked.connect(self.reload_user_list)
        refresh_btn.resize(30, 30)
        refresh_btn.move(470, 370)
        refresh_btn.setStyleSheet(
            'QPushButton {background-color: #ffffff; color: #2E2E2E; font: bold 14px; border-radius: 5px;}')

        # Drop down to choose user
        self.dropdown = QComboBox(self)
        self.dropdown.setEditable(True)
        self.dropdown.addItems(self.user_list)
        self.dropdown.move(380, 410)
        self.dropdown.resize(120, 30)
        self.dropdown.setStyleSheet("background-color: #fff")

        self.show()


    # Method to initialize new user dialog
    def new_user(self):
        import CreateUserUI
        self.adduser = CreateUserUI.CreateUser()
        self.adduser.show()

    # Method to initialize main user interface
    def init_main_UI(self):
        if self.dropdown.currentText() != "None":
            result = QMessageBox.question(self, "Message", "Do you wan to open user % s?" % self.dropdown.currentText(), QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                self.accept()
            else:
                QMessageBox.critical(self, "Message", "Please choose again")
        else:
            QMessageBox.warning(self, 'Error', 'Create new user first!')

    # Method to refresh users list
    def reload_user_list(self):
        file_path = os.path.join("Users")
        self.user_list = []
        self.user_list.extend(os.listdir(file_path))
        if self.user_list == []:
            self.dropdown.clear()
            self.dropdown.addItem("None")
        else:
            self.user_list = []
            self.user_list.extend(os.listdir(file_path))
            self.dropdown.clear()
            self.dropdown.addItems(self.user_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    workout = LoginWindow()
    if workout.exec_() == QDialog.Accepted:
        import MainWindow
        mainwindow = MainWindow.MainWindow(workout.chosen_user)
        mainwindow.show()
    sys.exit(app.exec_())

