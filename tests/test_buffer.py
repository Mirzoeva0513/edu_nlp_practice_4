from dataclasses import dataclass
from typing import Any, Sequence, Generator

import pytest

from task_buffer import Buffer


@dataclass
class InputOutput:
    __Inputs = tuple[int, ...]
    __Output = str

    inputs: __Inputs
    output: __Output

    def __iter__(self) -> Generator[tuple[__Inputs, __Output], Any, None]:
        yield self.inputs, self.output


@dataclass
class InputsPart:
    __Inputs = tuple[int, ...]

    inputs: __Inputs
    part: tuple[int, ...]

    def __iter__(self) -> Generator[tuple[__Inputs, tuple[int, ...]], Any, None]:
        yield self.inputs, self.part


@pytest.mark.parametrize(
    "cases",
    [
        [
            InputOutput((1, 2, 3), ""),
            InputOutput((1, 2), "9"),
            InputOutput((8, 6, 5, 2, 1, 3), "22"),
        ],
    ],
)
def test_buffer_io(
    cases: list[InputOutput], capfd: pytest.CaptureFixture["str"]
) -> None:
    buffer = Buffer()

    for io in cases:
        for inputs, expected_out in io:
            buffer.add(*inputs)
            out, err = capfd.readouterr()
            out = out.strip("\n")
            assert out == expected_out and not err


@pytest.mark.parametrize(
    "cases",
    [
        [
            InputsPart((1, 2, 3), (1, 2, 3)),
            InputsPart((1, 2), ()),
            InputsPart((8, 6, 5, 2, 1, 3), (3,)),
        ],
    ],
)
def test_buffer_internal(cases: list[InputsPart]) -> None:
    buffer = Buffer()

    for inputs_part in cases:
        for inputs, expected_part in inputs_part:
            buffer.add(*inputs)
            actual_part = buffer.get_current_part()
            assert tuple(actual_part) == expected_part
