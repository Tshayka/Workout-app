import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.initUI(user)

        self.user = user


    def initUI(self, user):
        self.statusBar().showMessage('Ready')
        self.showMaximized()
        self.setWindowTitle("Extreme Workout - %s" % user)
        self.setWindowIcon(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'))
        self.show()
        self.main_menu()


    def main_menu(self):
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        helpMenu = mainMenu.addMenu('Help')

        # Add exit button
        saveButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&Save", self)
        saveButton.setShortcut("Ctrl+S")
        saveButton.setStatusTip('Save the session')
        # exitButton.triggered.connect(self.close_application)
        fileMenu.addAction(saveButton)

        save_asButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&Save as", self)
        save_asButton.setShortcut("Ctrl+Shift+S")
        save_asButton.setStatusTip('Save the session')
        # exitButton.triggered.connect(self.close_application)
        fileMenu.addAction(save_asButton)

        exitButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip('Leave the app')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        new_userButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&New user", self)
        new_userButton.setShortcut("Ctrl+N")
        new_userButton.setStatusTip('Leave The App')
        # exitButton.triggered.connect(self.close_application)
        editMenu.addAction(new_userButton)

        helpButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&Help", self)
        helpButton.setShortcut("F1")
        helpButton.setStatusTip('How to use this program')
        # exitButton.triggered.connect(self.close_application)
        helpMenu.addAction(helpButton)

        about_usButton = QAction(QIcon(os.getcwd() + '\graphics' + '\workout _logo_small.png'), "&About us", self)
        about_usButton.setShortcut("Ctrl+A")
        about_usButton.setStatusTip('Credits')
        # exitButton.triggered.connect(self.close_application)
        helpMenu.addAction(about_usButton)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    workout = MainWindow(user="DEVELOPER")
    sys.exit(app.exec_())