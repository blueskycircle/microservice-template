import pytest
from click.testing import CliRunner
from cli import cli

# pylint: disable=redefined-outer-name
# This disables the redefined-outer-name warning specifically for pytest fixtures

@pytest.fixture
def runner():
    """Fixture providing a CLI runner."""
    return CliRunner()


def test_cli_exists(runner):
    """Test that the CLI exists and can be invoked."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "math operations" in result.output
    assert "addition" in result.output
    assert "subtraction" in result.output


def test_addition_command(runner):
    """Test the addition command with various inputs."""
    # Test with positive integers
    result = runner.invoke(cli, ["addition", "2", "3"])
    assert result.exit_code == 0
    assert "5.0" in result.output

    # Test with negative numbers (use '--' separator)
    result = runner.invoke(cli, ["addition", "--", "-1", "1"])
    assert result.exit_code == 0
    assert "0.0" in result.output

    # Test with decimals
    result = runner.invoke(cli, ["addition", "2.5", "3.5"])
    assert result.exit_code == 0
    assert "6.0" in result.output


def test_addition_command_precision(runner):
    """Test the addition command with floating point precision edge cases."""
    # Test cases that would normally have floating point precision issues
    result = runner.invoke(cli, ["addition", "--", "-1", "2.3"])
    assert result.exit_code == 0
    assert "1.3" in result.output
    
    # Test more precision edge cases
    result = runner.invoke(cli, ["addition", "0.1", "0.2"])
    assert result.exit_code == 0
    assert "0.3" in result.output
    
    result = runner.invoke(cli, ["addition", "0.1", "0.7"])
    assert result.exit_code == 0
    assert "0.8" in result.output


def test_subtraction_command(runner):
    """Test the subtraction command with various inputs."""
    # Test with positive integers
    result = runner.invoke(cli, ["subtraction", "5", "3"])
    assert result.exit_code == 0
    assert "2.0" in result.output

    # Test with negative numbers
    result = runner.invoke(cli, ["subtraction", "1", "1"])
    assert result.exit_code == 0
    assert "0.0" in result.output

    # Test with decimals
    result = runner.invoke(cli, ["subtraction", "10.5", "4.5"])
    assert result.exit_code == 0
    assert "6.0" in result.output

    # Test with negative result
    result = runner.invoke(cli, ["subtraction", "3", "7"])
    assert result.exit_code == 0
    assert "-4.0" in result.output


def test_subtraction_command_precision(runner):
    """Test the subtraction command with floating point precision edge cases."""
    # Test cases that would normally have floating point precision issues
    result = runner.invoke(cli, ["subtraction", "1.3", "1"])
    assert result.exit_code == 0
    assert "0.3" in result.output
    
    # Test more precision edge cases
    result = runner.invoke(cli, ["subtraction", "0.3", "0.1"])
    assert result.exit_code == 0
    assert "0.2" in result.output
    
    result = runner.invoke(cli, ["subtraction", "1", "0.7"])
    assert result.exit_code == 0
    assert "0.3" in result.output


def test_invalid_inputs(runner):
    """Test error handling for invalid inputs."""
    # Test with non-numeric input for addition
    result = runner.invoke(cli, ["addition", "abc", "3"])
    assert result.exit_code != 0

    # Test with missing arguments for addition
    result = runner.invoke(cli, ["addition", "5"])
    assert result.exit_code != 0

    # Test with non-numeric input for subtraction
    result = runner.invoke(cli, ["subtraction", "xyz", "3"])
    assert result.exit_code != 0

    # Test with missing arguments for subtraction
    result = runner.invoke(cli, ["subtraction", "5"])
    assert result.exit_code != 0
