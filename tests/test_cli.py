from click.testing import CliRunner
from mmdesigner.cli import cli
from mmdesigner.cli import Environment


def test_cli_environment():
    env = Environment()
    assert not env.debug


def test_cli_test_model_status(testenv):
    """Test cli summary report"""
    runner = CliRunner()
    result = runner.invoke( cli, ["status"])
    assert result.exit_code == 0
    assert "Design summary" in result.output


def test_cli_app_version():
    """test cli version option"""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "cli, version" in result.output


def test_cli_help_option():
    """test cli help option"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output

# test individual commands

def test_Generator_cmd():
    """Test Generator"""
    assert 1 == 1
