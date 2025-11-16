import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        # Label (created only once)
        self.label = QLabel("Hello PyQt5!", self)
        self.label.setGeometry(150, 300, 200, 150)
        self.label.setStyleSheet("font-size: 30px;")

        # Button
        self.button = QPushButton("Click Me", self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText("Button Clicked!")
        print("button is clicked")
        self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
