import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def is_positive(num):
    return num > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-2) is False

def divide(a, b):
    return a / b
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

def greet(name):
    return f"Привет, {name}!"

def test_greet():
    assert greet("Анна") == "Привет, Анна!"

def get_even_numbers(lst):
    return [i for i in lst if i % 2 == 0]

def test_even_numbers():
    assert get_even_numbers([1,2,3,4,5,6]) == [2, 4, 6]

def reverse_string(s):
    return s[::-1]

def test_reverse_strings():
    assert reverse_string("Python") == "nohtyP"