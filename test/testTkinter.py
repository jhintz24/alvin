import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi

        self.quit = tk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit['fg'] = 'blue'

        self.quit.pack()
        self.hi_there.pack()

    def say_hi(self):
        self.quit['text'] = 'oops'
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("300x200+300+300")
app = Application(master=root)
app.mainloop()