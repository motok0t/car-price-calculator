"""
Утилиты для сохранения истории расчётов (опционально).
"""

import json
from datetime import datetime


def save_calculation(model: str, car_price: float, result: dict, filename="history.json"):
    """Сохраняет расчёт в JSON."""
    record = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "price": car_price,
        "final": result["final_price"]
    }
    
    try:
        with open(filename, "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    
    history.append(record)
    with open(filename, "w") as f:
        json.dump(history, f, indent=2)
