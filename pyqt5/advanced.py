import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
import os 

file_path = os.path.dirname(__file__)
image = os.path.join(file_path, "qwe.png")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled PyQt5 Window")
        self.setGeometry(200, 100, 600, 600)
        self.setWindowIcon(QIcon(image))

        # ---------- LABEL ----------
        label = QLabel("Hello Abushe 😊", self)
        label.setFont(QFont("Arial", 28))
        label.setGeometry(100, 200, 450, 80)
        label.setObjectName("mainLabel")   # For CSS styling

        # ---------- APPLY CSS ----------
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;         /* Dark modern background */
            }

            QLabel#mainLabel {
                color: #f8f8f2;                     /* Light text */
                background-color: #44475a;          /* Card style */
                padding: 20px;
                border-radius: 12px;
                border: 2px solid #6272a4;
            }

            QLabel#mainLabel:hover {
                background-color: #6272a4;
                color: white;
                border: 2px solid #50fa7b;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
