import tkinter as tk


class Gui():

    def __init__(self, width, height):
        self.root = tk.Tk()
        self.width = width
        self.height = height
        self.root.title('mmdesigner')
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

    def run(self):
        print("mmdesigner starting...")
        self.root.mainloop()

    def quit(self):
        print("mmdesigner terminating...")
        self.root.destroy()

