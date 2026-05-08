"""
Тесты для калькулятора авто.
Запуск: python tests/test_calculator.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from car_calculator import calculate_final_price, get_model_category  # noqa: E402


def test_calculate_final_price():
    result = calculate_final_price(1_000_000)

    assert result["car_price"] == 1_000_000
    assert result["customs"] == 480_000
    assert result["logistics"] == 150_000
    assert result["commission"] == (1_000_000 + 480_000 + 150_000) * 0.07
    assert result["final_price"] == 1_000_000 + 480_000 + 150_000 + result["commission"]


def test_get_model_category():
    assert get_model_category("BMW X5") == "премиум"
    assert get_model_category("Kia Rio") == "экономичная"
    assert get_model_category("Tesla Model 3") == "стандартная"


def test_edge_cases():
    result = calculate_final_price(100_000)
    assert result["final_price"] > 0

    result = calculate_final_price(50_000_000)
    assert result["final_price"] > 0


if __name__ == "__main__":
    test_calculate_final_price()
    test_get_model_category()
    test_edge_cases()
    print("✅ Все тесты пройдены!")
