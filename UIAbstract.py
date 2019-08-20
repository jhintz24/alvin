from PyQtWriter import PyQtWriter
from TkinterWriter import TkinterWriter

class UIAbstract:

    def __init__(self):
        self.buttons = []
        self.labels = []
        self.buttonId = 0
        self.labelId = 0

    def addButton(self, title, position):
        newButton = Button(title, position)
        newButton.id = self.buttonId
        self.buttonId += 1
        self.buttons.append(newButton)

    def addLabel(self, title, position):
        newLabel = Label(title, position)
        newLabel.id = self.labelId
        self.labelId += 1
        self.labels.append(newLabel)

    def updateButton(self, id=None, title=None, color=None):
        if not id:
            button = self.buttons[-1]
        if title:
            button.title = title
        if color:
            button.color = color

    def writeToPyQt(self):
        writer = PyQtWriter(self)
        writer.write()

    def writeToTkinter(self):
        writer = TkinterWriter(self)
        writer.write()


class Button:

    def __init__(self, title, position):
        self.id = 0
        self.title = title
        self.color = ''
        self.position = position
        self.signal = ''


class Label:

    def __init__(self, title, position):
        self.id = 0
        self.title = title
        self.position = position