import os

class TkinterWriter:

    def __init__(self, uiStructure):
        self.uiStructure = uiStructure

    def write(self, appName):

        if os.path.exists(appName):
            os.system('rm ' + appName)

        triggerButton = None

        with open(appName, 'a') as f:
            f.write('import tkinter as tk\n')
            f.write('class Application(tk.Frame):\n')
            f.write('    def __init__(self, master=None):\n')
            f.write('        super().__init__(master)\n')
            f.write('        self.master = master\n')
            f.write('        self.pack()\n')

            if len(self.uiStructure.buttons) > 0 or len(self.uiStructure.labels) > 0:
                f.write('        self.createWidgets()\n')
                f.write('    def createWidgets(self):\n')

            for button in self.uiStructure.buttons:
                f.write(f'        self.button{button.id} = tk.Button(self)\n')
                if button.title:
                    f.write(f'        self.button{button.id}["text"] = "{button.title}"\n')
                if button.color:
                    f.write(f'        self.button{button.id}["fg"] = "{button.color}"\n')
                if button.trigger:
                    f.write(f'        self.button{button.id}["command"] = self.command{button.id}\n')
                    triggerButton = button
                if button.position:
                    f.write(f'        self.button{button.id}.pack(side=\"{button.position}\")\n')
                else:
                    f.write(f'        self.button{button.id}.pack()\n')

            for label in self.uiStructure.labels:
                f.write(f'        self.label{label.id} = tk.Label(self)\n')
                if label.title:
                    f.write(f'        self.label{label.id}["text"] = "{label.title}"\n')
                if label.color:
                    f.write(f'        self.label{label.id}["fg"] = "{label.color}"\n')
                if label.position:
                    f.write(f'        self.label{label.id}.pack(side=\"{label.position}\")\n')
                else:
                    f.write(f'        self.label{label.id}.pack()\n')

            if triggerButton:
                f.write(f'    def command{button.id}(self):\n')
                if button.trigger['object'] == 'label':
                    f.write(f'        self.label0["text"] = \"{button.trigger["title"]}\"\n')
                elif button.trigger['object'] == 'button':
                    f.write(f'        self.button0["text"] = \"{button.trigger["title"]}\"\n')


            f.write('root = tk.Tk()\n')
            f.write('root.geometry("300x300+300+300")\n')
            f.write('app = Application(master=root)\n')
            f.write('app.mainloop()\n')