from foobar25 import solution


def test_normal():
    assert solution([2, 3, 4, 0]) == '24'


def test_with_one_neg():
    assert solution([2, 3, 4, -5]) == '24'


def test_starting_with_one_neg():
    assert solution([-2, 3, 4, 2]) == '24'


def test_starting_with_zero():
    assert solution([0, 3, 4, 2]) == '24'


def test_all_zero():
    assert solution([0, 0, 0, 0]) == '0'


def test_starts_zero_and_fraction():
    assert solution([0, 0, 0, 0.34]) == '0.34'


def test_starts_fraction_and_zero():
    assert solution([0.34, 0, 0]) == '0.34'


def test_mul_fractions():
    assert solution([0.34, 0, 0.56]) == '0.56'


def test_neg_fraction_start_then_zero():
    assert solution([-0.34, 0, 0]) == '0'


def test_zero_start_then_neg_fraction():
    assert solution([0, 0, -0.45]) == '0'


def test_zero_start_then_double_neg_fraction():
    assert solution([0, 0, -0.875, -0.45]) == '0.39375'


def test_odd_number_of_neg_fracs():
    assert solution([-0.25, -0.5, -0.125]) == '0.125'