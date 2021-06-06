import logging
import os
import sys
from mmdesigner import __version__
from mmdesigner.OpenSCAD import OpenSCAD
from mmdesigner.TreeWalker import TreeWalker
from mmdesigner.Generator import Generator
from stl import __about__

import click
from click_default_group import DefaultGroup

CONFIG_FILE = "mmdesigner.yml"

def print_version(ctx, param, value):
    """Display version info for app and major dependencies"""
    if not value or ctx.resilient_parsing:
        return
    osc = OpenSCAD()
    osc_version = osc.get_version()
    stl_version = __about__.__version__
    click.echo(f"mmdesigner version: {__version__}")
    click.echo(f"\tOpenSCAD version: {osc_version}")
    click.echo(f"\tnumpy_stl version: {stl_version}")
    ctx.exit()

class Environment:
    """Management class holding cli command context data"""

    def __init__(self):
        """Set initial context"""
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

@click.group(cls=DefaultGroup, default="summary", default_if_no_args=True)
@click.option(
            "--versions",
            help="Display version info and exit.",
            is_flag=True,
            expose_value=False,
            is_eager=True,
            callback=print_version
)
@click.option(
        "--model_path",
        help="Path to directory containing model to work on."
)
@click.option(
        "--model_name",
        help="Name of model in model_path to work on."
)
@pass_environment
def cli(ctx, model_path, model_name):
    if not model_path is None:
        ctx.model_path = model_path
    if not model_name is None:
        ctx.model_name = model_name

@cli.command(help = "Generating part STL files")
@click.option("--all", is_flag=True, help="Force generating part and assembly STL files.")
@click.option("--inv", is_flag=True, help="Generate inventory list.")
@pass_environment
def stl(ctx, all, inv):
    """Generate STL command"""
    click.echo(f"Running... all={all}")
    inv_path = os.path.join(ctx.model_path, ctx.model_name)
    if inv:
        tw = TreeWalker(inv_path, 'scad', None)
        click.echo("Generating inventory:")
        click.echo(f"\tModel Path: {ctx.model_path}, Model name: {ctx.model_name}")
        click.echo("\tParts list:")
        inv_parts = tw.get_leaf_file_list()
        for f in inv_parts:
            part_name = str(f)[len(inv_path):]
            click.echo(f"\t\t{part_name}")
        click.echo("\tAssembly list:")
        asm_list = tw.get_non_leaf_file_list()
        for f in asm_list:
            asm_name = str(f)[len(inv_path):]
            click.echo(f"\t\t{asm_name}")
            sys.exit(0)
    gen = Generator(inv_path)
    if all:
        click.echo("generating STL files for parts and assemblies")
        gen.run_all("stl")
    else:
        click.echo("generating STL files for parts only")
        gen.run_leaf_stl("stl")



@cli.command(help="Analyze design")
@click.option("--all", is_flag=True, help="generate part and assembly property files.")
@pass_environment
def analyze(ctx, all):
    """Analyze design command"""
    inv_path = os.path.join(ctx.model_path, ctx.model_name)
    gen = Generator(inv_path)
    if all:
        click.echo("Generating Property files for parts")
        gen.run_all("mass")
    else:
        click.echo("Generating mass property files for parts and assemblies")
        gen.run_leaf_stl("mass")

@cli.command(help="Generate PDF templates")
@click.option("--all", is_flag=True, help="Generate full PDF plan.")
@pass_environment
def plan(ctx):
    click.echo(f"Generating PDF templates for  {ctx.model_name}")

@cli.command(help="Display model summary")
@pass_environment
def summary(ctx):
    inv_path = os.path.join(ctx.model_path, ctx.model_name)
    tw = TreeWalker(inv_path, 'scad', None)
    click.echo("Generating inventory:")
    click.echo(f"\tModel Path: {ctx.model_path}, Model name: {ctx.model_name}")
    click.echo("\tParts list:")
    inv_parts = tw.get_leaf_file_list()
    for f in inv_parts:
        part_name = str(f)[len(inv_path):]
        click.echo(f"\t\t{part_name}")
    click.echo("\tAssembly list:")
    asm_list = tw.get_non_leaf_file_list()
    for f in asm_list:
        asm_name = str(f)[len(inv_path):]
        click.echo(f"\t\t{asm_name}")
        sys.exit(0)

@cli.command(help="Generate design Excel spreadsheet.")
@pass_environment
def gen_excel(ctx):
    inv_path = os.path.join(ctx.model_path, ctx.model_name)
    gen = Generator(inv_path)
    gen.gen_excel(ctx.model_name)
