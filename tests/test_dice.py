# -*- coding: utf-8 -*-
import pytest
import task_dice


def test_die_default():
    d6 = task_dice.Die()
    for _ in range(100):
        throw = d6.roll()
        assert 1 <= throw <= 6


@pytest.mark.parametrize("sides", (16, 20))
def test_die_custom(sides: int):
    die = task_dice.Die(sides)
    for _ in range(100):
        throw = die.roll()
        assert 1 <= throw <= sides
