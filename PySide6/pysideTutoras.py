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

        line_edit = QLineEdit()
        text_edit = QTextEdit()

        combobox = QComboBox() # Combobox é um dropdown, tem que adicionar os items
        combobox.addItems(["Verstappen", "Alonso", "Hamilton"])

        listwidget = QListWidget()
        listwidget.addItems(['ni hao', 'wangzi','ma'])

        slider = QSlider() #pra deixar o slider na horizontal só fazer isso slider = QSlider(Qt.Horizontal) 
        slider.setRange(0, 100) 

        inner_container= QWidget()
        inner_layout = QHBoxLayout(inner_container) # Orientação do layout, em QHBoxLayout o layout.addwidget mais acima é o mais a esquerda # QHBoxLayout displays horizontally 

        checkbox = QCheckBox('One') # Diferença: CheckBox tu pode marcar quantos quiser; RadioButton só pode 1  
        checkbox1 = QCheckBox('Two')
        checkbox2 = QCheckBox('Three')

        inner_layout.addWidget(checkbox)
        inner_layout.addWidget(checkbox1)
        inner_layout.addWidget(checkbox2)

        layout.addWidget(label)
        layout.addWidget(combobox)
        layout.addWidget(listwidget)
        layout.addWidget(text_edit)
        layout.addWidget(line_edit)
        layout.addWidget(button)
        layout.addWidget(inner_container)
        layout.addWidget(slider)
        


        
app = QApplication()
window = MainWindow()
window.show()
app.exec()