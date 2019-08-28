import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.button0 = tk.Button(self)
        self.button0["text"] = "-PRON- name"
        self.button0.pack()
        self.button1 = tk.Button(self)
        self.button1["text"] = "-PRON- name"
        self.button1.pack()
root = tk.Tk()
root.geometry("300x300+300+300")
app = Application(master=root)
app.mainloop()
