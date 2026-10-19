amount = float(input("Сума замовлення, грн: "))
weight = float(input("Маса, кг: "))
distance = float(input("Відстань, км: "))
fragile = input("Товар крихкий? (так/ні): ").strip().lower()

invalid_data = (
    amount < 0
    or weight <= 0
    or distance < 0
    or fragile not in ("так", "ні")
)

is_pickup = distance == 0

fragile_too_heavy = fragile == "так" and weight > 10

free_courier = (
    amount >= 1500
    and distance <= 20
    and weight <= 15
)

if invalid_data:
    result = "некоректні дані"
elif is_pickup:
    result = "самовивіз"
elif fragile_too_heavy:
    result = "звичайна доставка недоступна"
elif free_courier:
    result = "безкоштовна кур'єрська доставка"
else:
    result = "платна кур'єрська доставка"

print(result)