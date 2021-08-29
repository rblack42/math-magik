from mmdesigner.cli import pass_environment
from mmdesigner.Generator import Generator
import os
import click


@click.command("status", short_help="Generate STL files for current model.")
@pass_environment
def cli(ctx):
    """Generate STL files for parts, optionally for assemblies."""
    model_path = ctx.model_path
    model_path = os.path.abspath(model_path)
    click.echo(f"Working model path: {model_path}")
    click.echo("Generating STL files...")
    gen = Generator(model_path)
    gen.process_parts("stl")
