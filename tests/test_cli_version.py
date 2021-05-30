from click.testing import CliRunner
from mmdesigner.cli import cli
from mmdesigner import __version__


def test_cli_version():
    """Test cli OCS version option"""
    runner = CliRunner()

    # Given mmdesigner is a valid python package

    # When we invoke the cli module with the version argument
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0

    # Then we have no errors, and the version number matches.
    version = result.output.split()[2]
    assert version == __version__
