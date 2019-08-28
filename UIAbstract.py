

class UIAbstract:

    def __init__(self):
        self.buttons = []
        self.labels = []
        self.buttonId = 0
        self.labelId = 0

    def addButton(self, title=None, color=None, position=None):
        if position:
            for label in self.labels:
                label.position = None
            for button in self.buttons:
                button.position = None

        newButton = Button(title=title, color=color, position=position)
        newButton.id = self.buttonId
        self.buttonId += 1
        self.buttons.append(newButton)

    def removeButton(self, id=None):
        del self.buttons[-1]

    def addLabel(self, title=None, color=None, position=None):
        if position:
            for label in self.labels:
                label.position = None
            for button in self.buttons:
                button.position = None

        newLabel = Label(title=title, color=color, position=position)
        newLabel.id = self.labelId
        self.labelId += 1
        self.labels.append(newLabel)

    def removeLabel(self, id=None):
        del self.labels[-1]

    def updateButton(self, id=None, title=None, color=None, position=None, trigger=None):
        if position:
            for label in self.labels:
                label.position = None
            for button in self.buttons:
                button.position = None

        button = self.buttons[-1]
        if title:
            button.title = title
        if color:
            button.color = color
        if position:
            button.position = position
        if trigger:
            button.trigger = trigger

    def updateLabel(self, id=None, title=None, color=None, position=None):
        if position:
            for label in self.labels:
                label.position = None
            for button in self.buttons:
                button.position = None

        label = self.labels[-1]
        if title:
            label.title = title
        if color:
            label.color = color
        if position:
            label.position = position


class Button:

    def __init__(self, title=None, color=None, position=None):
        self.id = 0
        self.title = title
        self.color = color
        self.position = position
        self.trigger = None


class Label:

    def __init__(self, title=None, color=None, position=None):
        self.id = 0
        self.title = title
        self.color = color
        self.position = position
