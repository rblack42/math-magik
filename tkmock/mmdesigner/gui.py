import tkinter as tk

class Gui(object):

    def __init__(self, root, name):
        self.root = root
        self.root.title(name)
        self.root.geometry("400x600")

    def run(self):
        self.root.mainloop()


