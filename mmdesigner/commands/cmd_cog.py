from mmdesigner.cli import pass_environment

import click


@click.command("status", short_help="Calculate model center of gravity.")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    click.echo("Calculating COG...")
