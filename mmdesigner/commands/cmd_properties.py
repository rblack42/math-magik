from mmdesigner.cli import pass_environment
from mmdesigner.Generator import Generator
import os

import click


@click.command("status", short_help="Calculate design properties for current model.")
@pass_environment
def cli(ctx):
    """Calcu;ate COG and MOI for model from sT: files. Generate STL files if needed"""
    click.echo("Calculating mass properties...")
    model_path = ctx.model_path
    model_path = os.path.abspath(model_path)
    click.echo(f"Working model path: {model_path}")
    click.echo("Generating Property json files...")
    gen = Generator(model_path)
    gen.process_parts("mass")
