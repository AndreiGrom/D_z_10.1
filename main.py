from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_function_eror(x, y):
    return x / y


my_function_eror(3, 0)