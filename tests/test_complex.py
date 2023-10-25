from operator import add, sub, mul, truediv
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from typing import Any, Callable

import pytest

from task_complex import Complex


BinaryOperation = Callable[[Any, Any], Any]


@pytest.mark.parametrize(
    "left, right, op, expected",
    [
        (Complex(1), Complex(1), add, 2),
        (Complex(3, 3), -3, add, Complex(0, 3)),
        (Complex(1), Complex(0, 1), sub, Complex(1, -1)),
        (Complex(1), Complex(2), mul, Complex(2)),
        (Complex(1), 2, mul, Complex(2)),
        (2, Complex(1, 3), mul, Complex(2, 6)),
        (Complex(1, 2), Complex(2, -3), mul, Complex(8, 1)),
        (1, Complex(1, 2), truediv, Complex(0.2, -0.4)),
    ],
)
def test_complex_operation(
    left: Complex | float,
    right: Complex | float,
    op: BinaryOperation,
    expected: Complex | float,
):
    actual = op(left, right)
    assert expected == actual


@pytest.mark.parametrize(
    "left, right, op, expectation",
    [
        (Complex(1, 2), 1, add, does_not_raise()),
        (-3, Complex(3, 4), truediv, does_not_raise()),
        (Complex(2, 3), "text", add, pytest.raises(TypeError)),
        (Complex(2, 3), 0, truediv, pytest.raises(ZeroDivisionError)),
    ],
)
def test_complex_raises(
    left: Any,
    right: Any,
    op: BinaryOperation,
    expectation: AbstractContextManager,
):
    with expectation:
        assert op(left, right)
