import click

import mmdesigner
from mmdesigner import __version__

@click.version_option(__version__, '--version')

@click.group()
@click.option('-m', '--model', help="Name of model in model path directory.")
@click.option('-d', '--model_dir', default = ".", help="Path to directory containing one or more models.")
def cli(model, model_dir):
    click.echo(f"Processing model: {model} in directory {model_dir}")


@click.command()
def hello():
    click.echo("hello")
