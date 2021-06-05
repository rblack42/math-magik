import logging
import os
import sys
from mmdesigner import __version__

import click
from click_default_group import DefaultGroup

CONFIG_FILE = "mmdesigner.yml"

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Version {__version__}")
    ctx.exit()

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        try:
            self.model_path = os.environ['MMDESIGNER_PATH']
        except: # pragma: no cover
            self.model_path = None
        try:
            self.model_name = os.environ['MMDESIGNER_MODEL']
        except: # pragma: no cover
            self.model_name = None

pass_environment = click.make_pass_decorator(Environment, ensure=True)

@click.group(cls=DefaultGroup, default="stl", default_if_no_args=True)
@click.option(
            "--version",
            help="Display version info and exit.",
            is_flag=True,
            expose_value=False,
            is_eager=True,
            callback=print_version
)
@pass_environment
def cli(ctx):
    pass

@cli.command(help = "Generating part STL files")
@click.option("--all", is_flag=True, help="Force generating part and assembly STL files.")
def stl(all):
    click.echo(f"Running... all={all}")

@cli.command(help="Analyze design")
@pass_environment
def analyze(ctx):
    click.echo(f"Analyzing path {ctx.home}")

@cli.command(help="Generate PDF templates")
@click.option("--all", is_flag=True, help="Generate full PDF plan.")
@pass_environment
def plan(ctx):
    click.echo(f"Generating PDF templates for  {ctx.model_name}")
