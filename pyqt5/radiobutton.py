import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button Example")
        self.setGeometry(500, 400, 500, 500)

        # Create radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("Gift Card", self)

        # Initialize UI properly
        self.initUI()

    def initUI(self):
        self.radio1.move(50, 50)
        self.radio2.move(50, 100)
        self.radio3.move(50, 150)

        # Connect radio button events
        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)
        self.radio3.toggled.connect(self.radio_changed)

    def radio_changed(self):
        if self.radio1.isChecked():
            print("Visa selected")
        elif self.radio2.isChecked():
            print("Master Card selected")
        elif self.radio3.isChecked():
            print("Gift Card selected")

# Main loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
