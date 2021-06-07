import os
import click


class Environment:
    """Context class holding state for cli commands"""
    def __init__(self):
        self.cwd = os.getcwd()
        self.part_count = 0
        self.assembly_count = 0
        self.model_path = "tests/test_data"
        self.model_name = "model"
        self.debug = False


pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "commands"
    )
)


class CLI(click.MultiCommand):
    """Modular CLI class"""
    def list_commands(self, ctx):
        """scan command directory and list all cli commands"""
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py"):
                if filename.startswith("cmd_"):
                    rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """import cli command file on demand"""
        try:
            mod = __import__(
                    f"mmdesigner.commands.cmd_{name}",
                    None,
                    None,
                    ["cli"]
            )
        except ImportError:
            return
        return mod.cli


@click.command(cls=CLI)
@click.option("--debug", is_flag=True, help="Enable debug output")
@pass_environment
def cli(ctx, debug):
    """primary CLI interface"""
    ctx.debug = debug
