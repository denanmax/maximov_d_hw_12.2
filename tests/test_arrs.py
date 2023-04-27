from utils import arrs
import unittest
import pytest

from utils.arrs import my_slice


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], 0) == None
    assert arrs.get([1, 2, 3], 5) == None
    assert arrs.get([1, 2, 3], -1, "wrong") == "wrong"
    assert arrs.get([1, 2, 3], 5, "wrong") == "wrong"
    assert arrs.get([100, 2000, 100_000], 2, "test") == 100_000


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert my_slice([]) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, -2) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, 5) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-1) == [1, 2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5], -10, 10) == [1, 2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], start=-1, end=3) == []




