from mmdesigner.cli import pass_environment

import click


@click.command("gen", short_help="Generate properties for current model.")
@pass_environment
def cli(ctx):
    """Generate mass cog and dimension properties for current model."""
    click.echo("Generating properties...")
