import pytest
from sys import argv
from src.sayit import main


usage = """usage: pytest [-h] word

Pronounce the given word

positional arguments:
  word        word to be pronounced

optional arguments:
  -h, --help  show this help message and exit
"""

suggestion = """soemthing seems to be not a correct word.
Is it possible that you meant any of these:
something • somethings • smoothing • seething • soothing • sleuthing • something's • seeming • mouthing • scything
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

    @pytest.mark.parametrize("test_input,expected", [("soemthing", 2)])
    def test_with_incorrect_word(self, capsys, test_input, expected):
        argv.pop()  # Remove --help
        argv.append(test_input)
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert captured.out == suggestion
        assert e.value.code == expected
