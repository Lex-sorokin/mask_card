import pytest

from src.decorators import foo, log


def test_log_error_console(capsys):
    @log()
    def foo(x, y):
        return x + y

    with pytest.raises(TypeError):
        foo(2, "3")
        captured = capsys.readouterr()
        assert "foo - <class 'TypeError'> - args: (3, '2') - kwargs: {}" == captured.out


def test_log_console(capsys):
    foo

    foo(2, 3)
    captured = capsys.readouterr()
    assert "foo - OK - 5\n\n" == captured.out


def test_log_success_file():

    file_name = "tests/test.txt"

    @log(filenane=file_name)
    def foo(x, y):
        return x + y

    result = foo(2, 3)
    assert result == 5

    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
        assert content[-1] == "foo - OK - 5\n"
