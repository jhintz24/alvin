from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.label = QLabel('ready...')  # self.count = 0
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        button = QPushButton('Push me')
        button.clicked.connect(self.buttonClicked)

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        grid.addWidget(button, 4, 0)
        grid.addWidget(self.label, 5, 0)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(grid)

        self.setWindowTitle('Review')
        self.show()

    def buttonClicked(self):
        print('button pressed')
        self.label.setText = 'hello'
        #self.count += 1


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()