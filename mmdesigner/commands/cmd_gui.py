from sys import platform
import click
import tkinter as tk
from mmdesigner.ui.gui import Gui
from mmdesigner.cli import pass_environment


@click.command("gui", short_help="Launch GUI interface.")
@pass_environment
def cli(ctx):
    """Launch GUI interface."""
    root = tk.Tk()
    width = 450 if platform == 'win32' else '600'
    size = f'{width}x470'
    gui = Gui(root, "mmdesigner", size)
    gui.run()


