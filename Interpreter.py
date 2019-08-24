import UIAbstract
import subprocess


class Interpreter:

    def __init__(self):
        self.uiAbstract = UIAbstract()
        self.oldProcess = None


    def processInput(self, input):
        if input.find('create') >= 0:
            self.runScript()
        if input.find('add') >= 0:
            if input.find('button') >= 0:
                title = input[input.find('title')+1:]
                self.uiAbstract.addButton(title, 'right')
                self.runScript()
        if input.find('make') >= 0:
            if input.find('button') >= 0:
                if input.find('title') >= 0:
                    title = input[input.find('title') + 1:]
                    self.uiAbstract.updateButton(title=title)
                if input.find('color') >= 0:
                    self.uiAbstract.updateButton(color='blue')
                self.runScript()


    def runScript(self):
        if self.oldProcess:
            self.oldProcess.kill()

        self.uiAbstract.writeToTkinter()
        self.oldProcess = subprocess.Popen(['python', 'app3.py'])