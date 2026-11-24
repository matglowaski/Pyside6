from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ronaldo")

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        helpMenu = menubar.addMenu('?')

        subMenu = fileMenu.addMenu('Submenu') #subMenu de fineMenu pra sair da aplicação
        exitAction = subMenu.addAction('Exit')
        exitAction.triggered.connect(exit)# ou um (self.close)

        aboutAction = helpMenu.addAction('About')
        aboutAction.triggered.connect(lambda: print('Tutorial GUI App'))# Mensagem aparece no terminal 
        
app = QApplication()
window = MainWindow()
window.show()
app.exec()