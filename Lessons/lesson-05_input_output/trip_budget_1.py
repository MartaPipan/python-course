distance_one_way = float(input("Відстань в один бік, км: "))
fuel_consumption = float(input("Витрата пального (л/100 км): "))
fuel_price = float(input("Ціна 1 літра (грн): "))
passengers = int(input("Кількість пасажирів: "))

total_distance = distance_one_way * 2
fuel_needed = total_distance * fuel_consumption / 100
total_cost = fuel_needed * fuel_price
cost_per_passenger = total_cost / passengers

full_canisters = int(fuel_needed // 20)
fuel_remainder = fuel_needed % 20


minimum_canisters = int(fuel_needed // 20 + (fuel_needed % 20 > 0))

print("\n--- Кошторис поїздки ---")
print(f"Повна відстань: {total_distance:.2f} км")
print(f"Потрібна кількість пального: {fuel_needed:.2f} л")
print(f"Загальна вартість пального: {total_cost:.2f} грн")
print(f"Внесок одного пасажира: {cost_per_passenger:.2f} грн")
print(f"Повних каністр по 20 л: {full_canisters}")
print(f"Залишок: {fuel_remainder:.2f} л")
print(f"Мінімальна кількість каністр: {minimum_canisters}")