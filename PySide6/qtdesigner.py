from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from Pyside6.QtUiTools import QUiLoader

app = QApplication

loader = QUiLoader()

file = QFile('file.ui') # Nome do file vindo do QtDesigner
file.open(QFile.ReadOnly)

window = loader.load(file)
file.close()
# Então para manipular os elementos procurar nome no QtDesigner  

window.show()
app.exec()