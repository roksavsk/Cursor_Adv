from calc import Calculator
import pytest


def test_add():
    assert Calculator.add(7.1, 5) == 12.1
    assert Calculator.add(-7, -3) == -10
    assert Calculator.add(105, 275) == 380
    with pytest.raises(TypeError):
        Calculator.add("a", 3)


def test_subtract():
    assert Calculator.subtract(7, 3) == 4
    assert Calculator.subtract(2, 9) == -7
    assert Calculator.subtract(20, 0) == 20
    with pytest.raises(TypeError):
        Calculator.subtract(1, "b")


def test_multiply():
    assert Calculator.multiply(7, 5) == 35
    assert Calculator.multiply(9, 9) == 81
    assert Calculator.multiply(-5, 11) == -55
    with pytest.raises(TypeError):
        Calculator.multiply("a", "b")


def test_divide():
    assert Calculator.divide(9, 3) == 3
    assert Calculator.divide(99, 11) == 9
    assert Calculator.divide(100, -5) == -20
    with pytest.raises(ValueError):
        assert Calculator.divide(5, 0)
    with pytest.raises(TypeError):
        Calculator.divide(5, "c")


if __name__ == '__main__':
    pytest.main()
