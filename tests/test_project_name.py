import pytest
from project_name import factorial


def test_factorial():
    assert factorial(15) == 1_307_674_368_000
