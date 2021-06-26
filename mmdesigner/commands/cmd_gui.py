from sys import platform
import click
import tkinter as tk
from mmdesigner.Gui import Gui
from mmdesigner.cli import pass_environment


@click.command("gui", short_help="Launch GUI interface.")
@pass_environment
def cli(ctx):
    """Launch GUI interface."""
    root = tk.Tk()
    gui = Gui(500,400)
    gui.run()


