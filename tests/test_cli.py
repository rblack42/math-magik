from click.testing import CliRunner
from mmdesigner.cli import cli
from mmdesigner.cli import Environment

from mmdesigner import __version__

def test_cli_environment():
    env = Environment()
    assert env.verbose == False


def test_cli_running():
    """Test cli reports running"""
    runner = CliRunner()
    result = runner.invoke(
                cli,
                [
                        "--model_path",
                        "tests/test_data",
                        "--model_name",
                        "model",
                        "summary"
                ]
    )
    assert result.exit_code == 0
    assert "Generating inventory" in result.output

def test_cli_version():
    """test cli version option"""
    runner = CliRunner()
    result = runner.invoke(cli, ["--versions"])
    assert result.exit_code == 0
    assert "mmdesigner version" in result.output

def test_cli_help_option():
    """test cli help option"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output
