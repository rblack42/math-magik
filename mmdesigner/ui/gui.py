import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Menu
from PIL import ImageTk
from tkinter.messagebox import showinfo


def donothing():
    print("nothing")

def selectfile():
    filetypes = (
        ('scad files', '*.scad'),
        ('all files', '*.*')
    )
    filename = fd.askopenfilenames(
        title='Open file',
        initialdir = '~/',
        filetypes=filetypes
    )

    showinfo(
        title='Selected file',
        message=filename
    )


def selectdir():
    dirpath = fd.askdirectory(
            title="Select project directory",
            initialdir='~/',
    )
    showinfo(
            title='selected directory',
            message=dirpath
    )
class Gui():

    def __init__(self, root, name, size):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title(name)
        self.root.withdraw()
        self.root.geometry(size)
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.configure()

    def run(self):
        print("mmdesigner starting...")
        self.root.mainloop()

    def quit(self):
        print("mmdesigner terminating")
        self.root.destroy()

    def configure(self):
        # set application icon
        iconphoto = "mmdesigner/ui/lpp.png"
        photo = ImageTk.PhotoImage(file=iconphoto)
        self.root.iconphoto(False, photo)

        # create manubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # add file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        filemenu.add_command(label="New", command=selectdir)
        filemenu.add_command(label="Open", command=selectfile)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(
                label="File",
                menu=filemenu
        )

        # add help menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Welcome')
        helpmenu.add_command(label='About...')

        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=helpmenu
        )
        self.root.deiconify()

if __name__ == '__main__':
    gui = Gui(tk.Tk())
    gui.configure()
    gui.run()
