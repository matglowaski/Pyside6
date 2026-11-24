from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ronaldo")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container) # QVBoxLayout displays vertically # Orientção do layout, em QVBoxLayout o layout.addWidget mais acima será o primeiro 
         # QGridLayout divide em partes, tem que settar row e colunm(0, 0) (0, 1)
        
        label = QLabel("Ronaldinho 1")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Dunk me")
        button.clicked.connect(lambda: print("button clicked"))

        listwidget = QListWidget()
        listwidget.addItems(['ni hao', 'wangzi','ma'])
        listwidget.itemClicked.connect(lambda item: print(f'item clicked {item.text()}'))
        listwidget.itemDoubleClicked.connect(lambda item: print(f'item double clicked {item.text()}'))


        inner_container= QWidget()
        inner_layout = QHBoxLayout(inner_container) # Orientação do layout, em QHBoxLayout o layout.addwidget mais acima é o mais a esquerda # QHBoxLayout displays horizontally 

        radio = QRadioButton('One') # Diferença: CheckBox tu pode marcar quantos quiser; RadioButton só pode 1  
        radio1 = QRadioButton('Two')
        radio2 = QRadioButton('Three')
        for r in(radio, radio1, radio2):
            r.toggled.connect(self.radio_changed)

        inner_layout.addWidget(radio)
        inner_layout.addWidget(radio1)
        inner_layout.addWidget(radio2)

        layout.addWidget(label)
        layout.addWidget(listwidget)
        layout.addWidget(button)
        layout.addWidget(inner_container)

    def radio_changed(self):
        r = self.sender() 
        if r.isChecked():
            print('radio button was selected. Value ', r.text())
    


        
app = QApplication()
window = MainWindow()
window.show()
app.exec()