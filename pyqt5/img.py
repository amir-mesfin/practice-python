import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import os 

file_path = os.path.dirname(__file__)
image = os.path.join(file_path, "qwe.png")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Image Viewer")
        self.setGeometry(300, 100, 700, 700)
        self.setWindowIcon(QIcon(image))

        # ----------- LABEL FOR IMAGE -----------
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        # Make label fill the window
        self.setCentralWidget(self.label)

        # ----------- CSS STYLE -----------
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }

            QLabel {
                border: 5px solid #6272a4;
                border-radius: 20px;
                background-color: #2a2a3c;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
