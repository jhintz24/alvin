import os

class PyQtWriter:

    def __init__(self, uiStructure):
        self.uiStructure = uiStructure

    def write(self):

        os.system('rm app2.py')

        with open('app2.py', 'a') as f:
            f.write('from PyQt5.QtGui import *\n')
            f.write('from PyQt5.QtWidgets import *\n')
            f.write('from PyQt5.QtCore import *\n')
            f.write('import sys\n')
            f.write('app = QApplication(sys.argv)\n')
            f.write('class MainWindow(QMainWindow):\n')
            f.write('    def __init__(self, *args, **kwargs):\n')
            f.write('        super(MainWindow, self).__init__(*args, **kwargs)\n')

            for button in self.uiStructure.buttons:
                f.write(f'        self.button{button.id} = QPushButton(\'{button.title}\')\n')
                f.write(f'        self.setCentralWidget(self.button{button.id})\n')

            for label in self.uiStructure.labels:
                f.write(f'        self.label{label.id} = QLabel({label.title})\n')

            f.write('window = MainWindow()\n')
            f.write('window.show()\n')
            f.write('app.exec_()\n')