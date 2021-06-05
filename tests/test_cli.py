from click.testing import CliRunner
from mmdesigner.cli import cli
from mmdesigner import __version__


def test_cli_running():
    """Test cli reports running"""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Running" in result.output

def test_cli_version():
    """test cli version option"""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "Version" in result.output

def test_cli_help_option():
    """test cli help option"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output
