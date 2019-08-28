from UIAbstract import UIAbstract
from TkinterWriter import TkinterWriter
import subprocess
import spacy
import json


class Interpreter:

    def __init__(self, appName):
        self.appName = appName
        self.uiAbstract = UIAbstract()
        self.oldProcess = None

    # Driver function
    def processInput(self, text):

        structure = self.parseText(text)
        print(structure)

        self.updateUi(structure)
        writer = TkinterWriter(self.uiAbstract)
        writer.write(self.appName)

        self.runApp()

    # Parse text into commands
    def parseText(self, text, structure=None):
        if not structure:
            structure = {}

        if type(text) is not list:
            nlp = spacy.load('en_core_web_sm')
            doc = nlp(text)

            text = []
            for token in doc:
                text.append(token.lemma_) # Currently has a problem with -PRON-
            print('TEXT', text)

        # Read in vocab
        with open('vocab.json') as json_file:
            vocab = json.load(json_file)

        # Tokenize
        tokenization = []
        for word in text:
            if word in vocab:
                tokenization.append(vocab[word])
            else:
                tokenization.append('')

        # Build structure from tokens
        if 'CONDITIONAL' in tokenization:
            index = tokenization.index('CONDITIONAL')
            structure['conditional'] = {}
            structure['conditional']['action'] = self.parseText(text[:index])
            structure['conditional']['trigger'] = self.parseText(text[index + 1:])

        elif 'OBJECT' in tokenization:
            structure['object'] = text[tokenization.index('OBJECT')]

            if 'ADD' in tokenization:
                structure['add'] = 1
            elif 'REMOVE' in tokenization:
                structure['remove'] = 1
            elif 'MODIFY' in tokenization:
                structure['modify'] = 1

            if 'ACTION' in tokenization:
                structure['action'] = text[tokenization.index('ACTION')]

            if 'POSITION' in tokenization:
                structure['position'] = text[tokenization.index('POSITION')]

            if 'SIZE' in tokenization:
                structure['size'] = text[tokenization.index('SIZE')]

            if 'COLOR' in tokenization:
                structure['color'] = text[tokenization.index('COLOR')]

            if 'ATTRIBUTE' in tokenization:
                index = tokenization.index('ATTRIBUTE')
                structure['title'] = ' '.join(text[index + 1:])

        return structure

    # Build the UI model from the structure outputted from parseText()
    def updateUi(self, update):

        if 'conditional' in update:
            if update['conditional']['trigger']['object'] == 'button':
                self.uiAbstract.updateButton(trigger={'title': update['conditional']['action']['title'],
                                                      'object': update['conditional']['action']['object']})

        elif 'add' in update or 'modify' in update:
            title = None
            color = None
            position = None
            if 'title' in update:
                title = update['title']
            if 'color' in update:
                color = update['color']
            if 'position' in update:
                position = update['position']

            if update['object'] == 'label':
                if 'add' in update:
                    self.uiAbstract.addLabel(title=title, color=color, position=position)
                if 'modify' in update:
                    self.uiAbstract.updateLabel(title=title, color=color, position=position)
            if update['object'] == 'button':
                if 'add' in update:
                    self.uiAbstract.addButton(title=title, color=color, position=position)
                if 'modify' in update:
                    self.uiAbstract.updateButton(title=title, color=color, position=position)

        elif 'remove' in update:
            if update['object'] == 'button':
                self.uiAbstract.removeButton()
            if update['object'] == 'label':
                self.uiAbstract.removeLabel()

    # Kill the currently app and run the new one
    def runApp(self):
        if self.oldProcess:
            self.oldProcess.kill()

        self.oldProcess = subprocess.Popen(['python', self.appName])