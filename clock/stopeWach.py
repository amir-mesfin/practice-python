import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QPushButton, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(500, 300, 400, 200)

        # Layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # Center label
        self.time_label.setAlignment(Qt.AlignCenter)

        # Dark theme CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 18px;
                font-family: Arial;
            }

            QLabel {
                font-size: 36px;
                font-weight: bold;
                padding: 15px;
                border: 2px solid #555;
                border-radius: 10px;
                background-color: #2e2e2e;
            }

            QPushButton {
                background-color: #444;
                border: 2px solid #666;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #666;
                border-color: #888;
            }

            QPushButton:pressed {
                background-color: #222;
            }
        """)

        # Connect buttons
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)  # Update every 10 ms
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00.00")
    
    def Format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds//10:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.Format_time(self.time))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    StopwatchWindow = Stopwatch()
    StopwatchWindow.show()
    sys.exit(app.exec_())
