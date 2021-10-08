import sys
from PyQt5.QtWidgets import (
        QWidget,
        QApplication
)

class Gui(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Math Magik Designer")

    def quit(self):
        print("mmdesigner terminating...")
        self.root.destroy()

