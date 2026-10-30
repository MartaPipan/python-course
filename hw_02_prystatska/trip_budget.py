distance = float(input("Відстань в один бік, км: "))
consumption = float(input("Витрата пального, л/100 км: "))
fuel_price = float(input("Ціна одного літра пального, грн: "))
passengers = int(input("Кількість пасажирів: "))

total_km = distance * 2

fuel_liters = (total_km * consumption )/ 100

total_fuel_cost = fuel_liters * fuel_price
price_per_person = total_fuel_cost / passengers
canisters = int(fuel_liters // 20)
rest = fuel_liters % 20

needed_canisters = canisters + bool(rest)

print(f"\nПовна відстань: {total_km:.2f} км")
print(f"Потрібно пального: {fuel_liters:.2f} л")
print(f"Загальна вартість: {total_fuel_cost:.2f} грн")
print(f"Вартість для одного пасажира: {price_per_person:.2f} грн")
print(f"Повних каністр: {canisters}")
print(f"Залишок: {rest:.2f} л")
print(f"Мінімальна кількість каністр: {needed_canisters}")