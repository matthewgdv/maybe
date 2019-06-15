import pytest
from maybe.maybe import Maybe


class Other:
    pass


class Example:
    name = "example"
    null = None


test_int = 1
test_float = 1.2
test_bool = True
test_string = "hi"
test_list = [1, 2, 3]
test_dict = {1: "one", 2: "two", 3: "three"}
test_set = {1, 2, 3}
test_types = [test_int, test_float, test_bool, test_string, test_list, test_dict, test_set]


@pytest.mark.parametrize(["value", "expected"], [(None, Other), *[(val, val) for val in test_types]])
def test_simple(value, expected):
    assert Maybe(value).else_(Other) == expected


@pytest.mark.parametrize(["value"], [(value,) for value in test_types])
def test_truthiness_simple_valid(value):
    assert Maybe(value)


def test_truthiness_complex_valid():
    assert Maybe(Example).null


def test_truthiness_simple_invalid():
    assert not Maybe(None)


def test_truthiness_complex_invalid():
    assert not Maybe(Example).monkeyweasel


def test_valid_item_access():
    key = list(test_dict)[0]
    assert Maybe(test_dict)[key].else_(Other) == test_dict[key]


def test_invalid_item_access():
    assert Maybe(test_dict)["monkeyweasel"].else_(Other) == Other


def test_valid_attribute_access():
    assert Maybe(test_dict).items.else_(Other) == test_dict.items


def test_invalid_attribute_access():
    assert Maybe(test_dict).monkeyweasel.else_(Other) == Other


def test_item_and_attribute_acess():
    assert Maybe(Example).name[1].else_(Other) == Example.name[1]


def test_valid_none():
    assert Maybe(Example).null.else_(Other) is None


def test_method_calls():
    assert Maybe(test_string).upper().else_(Other) == test_string.upper()


def test_addition():
    assert (Maybe(test_int) + test_int).else_(Other) == test_int*2


def test_reverse_addition():
    assert (test_int + Maybe(test_int)).else_(Other) == test_int*2


def test_subtraction():
    assert (Maybe(test_int) - test_int).else_(Other) == 0


def test_reverse_subtraction():
    assert (test_int - Maybe(test_int)).else_(Other) == 0


def test_multiplication():
    assert (Maybe(test_int)*test_int).else_(Other) == test_int**2


def test_reverse_multiplication():
    assert (test_int*Maybe(test_int)).else_(Other) == test_int**2


def test_division():
    assert (Maybe(test_int)/test_int).else_(Other) == 1


def test_reverse_division():
    assert (test_int/Maybe(test_int)).else_(Other) == 1


def test_floor_division():
    assert (Maybe(9) // 2).else_(Other) == 4


def test_reverse_floor_division():
    assert (9 // Maybe(2)).else_(Other) == 4


def test_modulo():
    assert (Maybe(11) % 4).else_(Other) == 3


def test_reverse_modulo():
    assert (11 % Maybe(4)).else_(Other) == 3
