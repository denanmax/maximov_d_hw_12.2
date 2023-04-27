from utils import arrs
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], 0) == None
    assert arrs.get([1, 2, 3], 5) == None
    assert arrs.get([1, 2, 3], -1, "wrong") == "wrong"
    assert arrs.get([1, 2, 3], 5, "wrong") == "wrong"
    assert arrs.get([100, 2000, 100000], 2, "test") == 100000


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, -2) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, 5) == [3, 4, 5]
