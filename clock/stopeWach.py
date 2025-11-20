import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                              QPushButton, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
  def __init__(self):
    super().__init__()
    self.time = QTime(0, 0, 0, 0)
    self.time_label = QLabel("00:00:00", self)
    self.start_button = QPushButton("Start", self)
    self.stop_button = QPushButton("stop", self)
    self.reset_button = QPushButton("reset", self)
    self.timer = QTimer(self)
    self.initUI()
    
    def initUI(self):
      pass
      
    def start(self):
      pass
    
    def stop(self):
      pass
    
    
    def reset(self):
      pass
    
    def Format_time(self):
      pass
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  Stopwatch = Stopwatch()
  Stopwatch.show()
  sys.exit(app.exec_())
  