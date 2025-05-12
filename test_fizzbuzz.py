import pytest
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    # 直接値で判断する実装
    mapping = {
        1: "1",
        3: "Fizz",
        5: "Buzz",
        15: "FizzBuzz",
    }

    for number in mapping.keys():
        assert fizzbuzz(number) == mapping[number]