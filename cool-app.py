import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.button0 = tk.Button(self)
        self.button0["text"] = "press"
        self.button0["fg"] = "red"
        self.button0["command"] = self.command0
        self.button0.pack(side="bottom")
        self.label0 = tk.Label(self)
        self.label0["text"] = "test"
        self.label0["fg"] = "blue"
        self.label0.pack()
    def command0(self):
        self.label0["text"] = "success"
root = tk.Tk()
root.geometry("300x300+300+300")
app = Application(master=root)
app.mainloop()
