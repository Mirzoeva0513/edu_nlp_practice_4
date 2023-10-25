# -*- coding: utf-8 -*-
import abc
import task_zoo


def test_animal_class():
    assert issubclass(task_zoo.Animal, abc.ABC)
    assert issubclass(task_zoo.Dolphin, task_zoo.Animal)
    assert issubclass(task_zoo.Zebra, task_zoo.Animal)


def test_zebra_attributes():
    zebra = task_zoo.Zebra()
    required_attrs = ("name", "age", "info")
    for attr in required_attrs:
        assert hasattr(zebra, attr)


def test_dolphin_attributes():
    dolphin = task_zoo.Dolphin(age=15)
    required_attrs = ("name", "age", "info")
    for attr in required_attrs:
        assert hasattr(dolphin, attr)
