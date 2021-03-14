import tkinter as tk


class Gui(tk.Tk):

    def __init__(self, name, size):
        super().__init__(className=name)
        self.title(name)
        self.withdraw()
        self.geometry(size)
        self.protocol('WM_DELETE_WINDOW', self.quit)

    def get_main_window(self):
        self.set_icon()
        return self

    def set_icon(self):
        photo = tk.PhotoImage(file='mmdesigner/lpp.png')
        self.iconphoto(False, photo)


    def quit(self):
        self.destroy()
