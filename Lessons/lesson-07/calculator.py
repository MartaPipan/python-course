number1 = float(input("Перше число: "))
operator = input("Операція (+, -, *, /): ")
number2 = float(input("Друге число: "))

if operator == "+":
    result = number1 + number2
    print("Результат:", result)

elif operator == "-":
    result = number1 - number2
    print("Результат:", result)

elif operator == "*":
    result = number1 * number2
    print("Результат:", result)

elif operator == "/":
    if number2 == 0:
        print("Помилка: на нуль ділити не можна")
    else:
        result = number1 / number2
        print("Результат:", result)

else:
    print("Невідома операція")