import click
from click.testing import CliRunner
from str_counter import main


def test_str_counter():

    runner = CliRunner()
    result = runner.invoke(main, ['P'])
    assert result.exit_code == 0
    assert result.output == """ char : total
' P ' : 1
"""
    result = runner.invoke(main, ["--count_numbers",'1'])
    assert result.exit_code == 0
    assert result.output == """Total numbers 1
' 1 ' : 1"""
