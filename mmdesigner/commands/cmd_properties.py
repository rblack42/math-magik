from mmdesigner.cli import pass_environment

import click


@click.command(
        "status",
        short_help="Calculate design properties for current model.")
@pass_environment
def cli(ctx):
    """Calcu;ate COG and MOI for model from STL files"""
    click.echo("Calculating mass properties...")
