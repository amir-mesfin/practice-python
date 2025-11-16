import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import os 

file_path = os.path.dirname(__file__)
image = os.path.join(file_path, "qwe.png")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 is working!")
        # self.resize(400, 300)
        self.setGeometry(0,0,600,600)
        self.setWindowIcon(QIcon(image))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
