"""
Расчёт стоимости авто с таможней, логистикой и комиссией.
"""

CUSTOMS_RATE = 0.48
LOGISTICS_FIXED = 150000
COMMISSION_RATE = 0.07


def calculate_final_price(car_price: float) -> dict:
    customs = car_price * CUSTOMS_RATE
    logistics = LOGISTICS_FIXED
    subtotal = car_price + customs + logistics
    commission = subtotal * COMMISSION_RATE
    final_price = subtotal + commission

    return {
        "car_price": car_price,
        "customs": customs,
        "logistics": logistics,
        "commission": commission,
        "final_price": final_price
    }


def get_model_category(model: str) -> str:
    model_lower = model.lower()
    premium = ["bmw", "mercedes", "audi", "lexus", "porsche"]
    economy = ["kia", "hyundai", "lada", "renault"]

    if any(k in model_lower for k in premium):
        return "премиум"
    if any(k in model_lower for k in economy):
        return "экономичная"
    return "стандартная"
