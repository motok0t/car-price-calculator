"""
CLI-калькулятор стоимости авто "под ключ".
"""

from car_calculator import calculate_final_price, get_model_category


def validate_price(price_str: str) -> float:
    """Проверяет корректность цены. Поддерживает запятые, пробелы, _ и точки как разделители тысяч."""
    import re
    cleaned = re.sub(r'[ ,_\.]', '', price_str)
    cleaned = cleaned.replace(',', '.')
    price = float(cleaned)
    if price <= 0:
        raise ValueError("Цена должна быть положительной")
    if price > 100_000_000:
        raise ValueError("Слишком большая сумма")
    return price


def main():
    print("\n" + "=" * 50)
    print("   КАЛЬКУЛЯТОР СТОИМОСТИ АВТО «ПОД КЛЮЧ»")
    print("=" * 50)
    print("Таможня 48% | Логистика 150к руб. | Комиссия 7%")
    print("-" * 50)

    model = input("Марка и модель (например, BMW X5): ").strip()
    if not model:
        print("Ошибка: модель не указана")
        return

    while True:
        try:
            price_str = input("Стоимость авто в рублях: ").strip()
            car_price = validate_price(price_str)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте ещё раз.")

    category = get_model_category(model)
    result = calculate_final_price(car_price)

    print("\n" + "-" * 50)
    print(f"Модель: {model} ({category})")
    print(f"Цена авто: {result['car_price']:,.2f} ₽")
    print(f"Таможня 48%: {result['customs']:,.2f} ₽")
    print(f"Логистика: {result['logistics']:,.2f} ₽")
    print(f"Комиссия 7%: {result['commission']:,.2f} ₽")
    print("=" * 50)
    print(f"ИТОГО «ПОД КЛЮЧ»: {result['final_price']:,.2f} ₽")
    print("=" * 50)


if __name__ == "__main__":
    main()
