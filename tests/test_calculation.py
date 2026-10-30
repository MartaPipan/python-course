import pytest
from hw_08_prystatska.study_tools.calculations import mean, clamp, weighted_sum
#«Стартуй з кореня, зайди в папку hw_08_prystatska, потім у study_tools, відкрий файл calculations і візьми звідти функції».


# функція mean()
def test_mean_positive_numbers():
    assert mean(1, 2, 3, 4) == 2.5

def test_mean_empty():
    assert mean() is None

def test_mean_negative_numbers():
    assert mean(-10, -20, -30) == -20


# функція clamp()
def test_clamp_with_positive_numbers():
    # Значення між 0 та 100
    assert clamp(50) == 50

def test_clamp_below_lower():
    # менше за lower(0) поверне lower(0)
    assert clamp(-5) == 0

def test_clamp_above_upper():
    #більше за upper (100) має поверне upper (100)
    assert clamp(150) == 100

def test_clamp_invalid_data():
    # lower > upper, функція повертає None
    assert clamp(50, lower=10, upper=5) is None


#функція weighted_sum() ---
def test_weighted_sum_correct():
    # (1*0.5) + (2*0.3) + (3*0.2) = 0.5 + 0.6 + 0.6 = 1.7
    assert weighted_sum([1, 2, 3], [0.5, 0.3, 0.2]) == pytest.approx(1.7)

def test_weighted_sum_different_lengths():
    # Якщо довжина списків різна, поверне None
    assert weighted_sum([1, 2], [0.5, 0.3, 0.2]) is None

def test_weighted_sum_empty():
    # Якщо один зі списків порожній, повернe None
    assert weighted_sum([], []) is None
