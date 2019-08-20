import os

class TkinterWriter:

    def __init__(self, uiStructure):
        self.uiStructure = uiStructure

    def write(self):

        os.system('rm tkinter-app-1.py')

        with open('tkinter-app-1.py', 'a') as f:
            f.write('import tkinter as tk\n')
            f.write('class Application(tk.Frame):\n')
            f.write('    def __init__(self, master=None):\n')
            f.write('        super().__init__(master)\n')
            f.write('        self.master = master\n')
            f.write('        self.pack()\n')
            f.write('root = tk.Tk()\n')
            f.write('root.geometry("300x300+300+300")\n')
            f.write('app = Application(master=root)\n')
            f.write('app.mainloop()\n')