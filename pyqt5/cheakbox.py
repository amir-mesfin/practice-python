import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox Exampleof this ")
        self.setGeometry(500, 400, 500, 500)

        # Create a checkbox
        self.checkbox = QCheckBox("Check me!", self)
        self.checkbox.move(50, 50)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state:
            print("Checked!")
        else:
            print("Unchecked!")

# Main loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
