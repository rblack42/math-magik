from mmdesigner.cli import pass_environment

import click


@click.command("status", short_help="Generate STL files for current model.")
@pass_environment
def cli(ctx):
    """Generate STL files for parts, optionally for assemblies."""
    click.echo("Generating sTL files...")
