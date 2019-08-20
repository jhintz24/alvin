import speech_recognition as sr
import subprocess
from UIAbstract import UIAbstract

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


if __name__ == "__main__":

    # Set the voice interpreter
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    interpreter = Interpreter()

    # Start listening and interpreting voice input
    while True:
        input = ''
        with mic as source:
            print("listening...")
            audio = recognizer.listen(source)

        print("sending input...")
        try:
            input = recognizer.recognize_google(audio)
            print(input)
        except sr.UnknownValueError:
            print("did not understand...")

        if input == 'exit':
            break

        interpreter.processInput(input)
