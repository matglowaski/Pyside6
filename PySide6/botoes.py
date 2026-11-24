from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QGridLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ronaldo")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QGridLayout(container)


        button = QPushButton('Ronaldos')
        button.clicked.connect(lambda: QMessageBox.information(self, 'Info', 'Ronaldinho, Rona e Ronaldo')) # O primeiro é title, o segundo text
        
        button1 = QPushButton('Sim ou Não, Galo')
        button1.clicked.connect(self.ask_yes_no)

        button2 = QPushButton('Mostrar Ronaldos')
        button2.clicked.connect(self.ask_questions)

        
        layout.addWidget(button, 0, 0)
        layout.addWidget(button1, 1,0)
        layout.addWidget(button2, 0, 1)


    def ask_yes_no(self):
        if QMessageBox.question(self, 'Question', 'Quer cheirar?') == QMessageBox.Yes: 
            print('Então cheira minha bilola')
        else:
            print('Que pena, fica pra próxima')

    def ask_questions(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('You choose')
        msg.setText('Select your favorite Ronaldo')

        rona = msg.addButton('Rona', QMessageBox.AcceptRole)        
        ronaldo =msg.addButton('Ronaldo', QMessageBox.AcceptRole)
        ronaldinho= msg.addButton('Ronaldinho', QMessageBox.AcceptRole)
        neyma= msg.addButton('Neymá', QMessageBox.AcceptRole)

        msg.exec()

        if msg.clickedButton() == rona:
            print("Rona ou Dona?")
        elif msg.clickedButton() == ronaldo:
            print('CR7 ou Nazário?')
        elif msg.clickedButton() == ronaldinho:
            print("A magia está no ar")
        else:
            print("Esse n é um Ronaldo, mas tudo bem")
        
app = QApplication()
window = MainWindow()
window.show()
app.exec()