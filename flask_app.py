"""Веб-калькулятор стоимости авто с таможней, логистикой и комиссией."""

import re

from flask import Flask, render_template_string, request

from car_calculator import calculate_final_price, get_model_category

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор стоимости авто</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; max-width: 700px; margin: 50px auto; padding: 20px; }
        input, button { padding: 8px; margin: 5px; }
        .result { background: #f0f0f0; padding: 15px; margin-top: 20px; border-radius: 5px; }
        .info { background: #e8f4f8; padding: 15px; margin-bottom: 20px; border-radius: 5px; font-size: 14px; }
        .info h3 { margin-top: 0; }
    </style>
</head>
<body>
    <h2>Калькулятор стоимости авто «под ключ»</h2>

    <div class="info">
        <h3>📋 Тарифы (ставки)</h3>
        <ul>
            <li>🚢 Логистика: <strong>150 000 ₽</strong> (фиксированная)</li>
            <li>🛃 Таможня: <strong>48%</strong> от стоимости авто</li>
            <li>💳 Комиссия: <strong>7%</strong> от (цена + таможня + логистика)</li>
        </ul>
        <p><small>✅ Поддерживаются форматы: 1500000, 1,500,000, 1.500.000, 1 500 000, 1_500_000</small></p>
    </div>

    <form method="POST">
        <label>Марка и модель:</label><br>
        <input type="text" name="model" required><br><br>

        <label>Стоимость авто (₽):</label><br>
        <input type="text" name="price" placeholder="Например: 1,500,000" required><br><br>

        <button type="submit">Рассчитать</button>
    </form>

    {% if result %}
    <div class="result">
        <h3>Результат для {{ result.model }} ({{ result.category }})</h3>
        <p>💰 Цена авто: {{ "%.2f"|format(result.car_price) }} ₽</p>
        <p>🛃 Таможня 48%: {{ "%.2f"|format(result.customs) }} ₽</p>
        <p>🚢 Логистика: {{ "%.2f"|format(result.logistics) }} ₽</p>
        <p>💳 Комиссия 7%: {{ "%.2f"|format(result.commission) }} ₽</p>
        <hr>
        <h3>✅ ИТОГО «ПОД КЛЮЧ»: {{ "%.2f"|format(result.final_price) }} ₽</h3>
    </div>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    """Главная страница с формой и расчётом."""
    if request.method == 'POST':
        model = request.form['model']
        price_str = request.form['price']

        cleaned = re.sub(r'[^0-9]', '', price_str)
        car_price = int(cleaned)

        category = get_model_category(model)
        result_data = calculate_final_price(car_price)

        result = {
            'model': model,
            'category': category,
            'car_price': result_data['car_price'],
            'customs': result_data['customs'],
            'logistics': result_data['logistics'],
            'commission': result_data['commission'],
            'final_price': result_data['final_price']
        }
        return render_template_string(HTML_TEMPLATE, result=result)

    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run()
