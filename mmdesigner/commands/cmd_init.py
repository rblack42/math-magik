from mmdesigner.cli import pass_environment

import click

def create_standard_model(model_path):
    """Set standard model parts in place."""
    pass

@click.command("init", short_help="Initializes a model directory with standard parts.")
@click.argument("path", required=False, type=click.Path(resolve_path=True))
@pass_environment
def cli(ctx, path):
    """Initializes a repository."""
    if path is None:
        path = ctx.model_path
    click.echo(f"Initialized the repository in {click.format_filename(path)}")
