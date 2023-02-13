from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton,QTextEdit
from PyQt6 import QtCore

class MyWindow(QMainWindow):
    def __init__(self,width=500, height = 500, title="Qt") -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(250, 250, width, height)
        self.main_btn = QPushButton("Button1",self)
        self.main_lbl = QLabel("<b> This is Label</b>",self)
        self.main_btn.setGeometry(width//2, height//2, width,30)
        self.main_btn.adjustSize()
        self.main_lbl.setGeometry(width//2, height//2-100, width,100)
        self.main_lbl.adjustSize()
        self.main_btn.clicked.connect(QApplication.quit)
    def change_lable_text(self):
        self.main_lbl.setText("<b> Changed </b>")