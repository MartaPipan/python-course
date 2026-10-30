counter = 1

while counter <= 3:
    print(counter)
    counter += 1

print("Готово")


counter = 1
      ↓
counter <= 3 ?
      ↓
    True
      ↓
 print(counter)
      ↓
 counter += 1
      ↓
 перевірка знову
      ↓
counter <= 3 ?
      ↓
    True
      ↓
    ...
      ↓
counter = 4
      ↓
4 <= 3 → False
      ↓
  "Готово"

  Частина	Код      	     Для чого
1. Початок	counter = 1	    Звідки починаємо
2. Умова	counter <= 3	Коли продовжуємо
3. Зміна	counter += 1	Як рухаємося до завершення