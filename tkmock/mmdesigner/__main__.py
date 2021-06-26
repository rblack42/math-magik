import tkinter as tk
from mmdesigner.gui import Gui

if __name__ == '__main__':
    root = tk.Tk()
    gui = Gui(root, "mmdesigner")
    gui.run()

