import pytest
from src.decorators import log
import os


def test_log_console(capsys):
    @log()
    def example_function(x, y):
        return x * y
    result = example_function(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "example_function ok. Result: 6\n"
    assert result == 6
def test_log_file():
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y
    result = example_function(2, 3)
    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line
    assert log_string == "example_function ok. Result: 6\n"
    assert result == 6


def test_log_file_raise():
    @log(filename="mylog.txt")
    def example_function(x, y):
        raise TypeError("Что-то пошло не так")
    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(2, 10)
    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line
    assert log_string == "example_function TypeError: Что-то пошло не так. Inputs: (2, 10), {}\n"