import pytest
from sys import argv
from src.app import main


usage = """usage: pytest [-h] word

Pronounce the given word

positional arguments:
  word        word to be pronounced

optional arguments:
  -h, --help  show this help message and exit
"""


class TestCommandLine:
    def test_with_no_commands_or_option(self):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2

    def test_with_help_option(self, capsys):
        argv.append("--help")
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert captured.out == usage
        assert e.value.code == 0
