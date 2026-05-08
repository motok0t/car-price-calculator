"""Тесты для валидации ввода и определения категорий."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from car_calculator import get_model_category  # noqa: E402


def test_get_model_category():
    """Проверка определения категорий по ключевым словам."""
    # Премиум
    assert get_model_category("BMW X5") == "премиум"
    assert get_model_category("Mercedes S500") == "премиум"
    assert get_model_category("Audi A6") == "премиум"
    assert get_model_category("Lexus RX") == "премиум"
    assert get_model_category("Porsche Cayenne") == "премиум"

    # Экономичные
    assert get_model_category("Kia Rio") == "экономичная"
    assert get_model_category("Hyundai Solaris") == "экономичная"
    assert get_model_category("Lada Vesta") == "экономичная"
    assert get_model_category("Renault Logan") == "экономичная"

    # Стандартные (все остальные)
    assert get_model_category("Tesla Model 3") == "стандартная"
    assert get_model_category("Chery Tiggo") == "стандартная"
    assert get_model_category("Toyota Camry") == "стандартная"
    assert get_model_category("Ford Focus") == "стандартная"
    assert get_model_category("Haval Jolion") == "стандартная"


def test_get_model_category_case_insensitive():
    """Проверка, что регистр не влияет."""
    assert get_model_category("bmw x5") == "премиум"
    assert get_model_category("KIA RIO") == "экономичная"
    assert get_model_category("tEsLa mOdEl 3") == "стандартная"


def test_price_validation():
    """Проверка, что validate_price корректно обрабатывает разные форматы."""
    from main import validate_price

    assert validate_price("1500000") == 1500000
    assert validate_price("1,500,000") == 1500000
    assert validate_price("1.500.000") == 1500000
    assert validate_price("1 500 000") == 1500000
    assert validate_price("1_500_000") == 1500000
    assert validate_price("2,999,999") == 2999999


if __name__ == "__main__":
    test_get_model_category()
    test_get_model_category_case_insensitive()
    test_price_validation()
    print("✅ Все тесты валидации пройдены!")
