import main
import pytest


@pytest.mark.parametrize(
        ('input_x', 'input_x', 'expected'),
        (
            (0, 0, 1),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 2)
        )
)
def test_foo(input_x, input_y, expected):
    assert main.foo(input_x, input_y) == expected


def test_bar():
    assert main.bar(1, 1) == 4
