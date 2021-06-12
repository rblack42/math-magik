from mmdesigner.cli import pass_environment
import sys
import click


@click.command("status", short_help="Shows summary of current model.")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    click.echo("Design summary:")
    click.echo(f"\tCurrent working directory: {ctx.cwd}")
    click.echo(f"\tmodel_path: {ctx.model_path}")
    click.echo(f"\tmodel_name: {ctx.model_name}")
    click.echo(f"\tPart count: {ctx.part_count}")
    click.echo(f"\tAssembly count: {ctx.assembly_count}")
    click.echo(f"\tDebug: {ctx.debug}")
    sys.exit(0)
