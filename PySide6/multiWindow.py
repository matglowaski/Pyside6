from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtCore import Qt

class SecondaryWindow(QMainWindow):

    def __init__(self, n):
        super().__init__()
        self.setWindowTitle("Window Number n")

        label = QLabel(f'Number {n}')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ronaldo")

        button = QPushButton('Open secondary window')
        button.clicked.connect(self.open_window)

        self.setCentralWidget(button)

        self.count = 1
        self.windows = []

    def open_window(self):
        w = SecondaryWindow(self.count)

        self.count += 1
        self.windows.append(w)

        w.show()




        
app = QApplication()
window = MainWindow()
window.show()
app.exec()