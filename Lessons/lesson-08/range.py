print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(2, 8, 2))) # [2, 4, 6]
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1]

#Форми range():
#• range(stop) — від 0 до stop - 1;
#• range(start, stop) — від start до stop - 1;
#• range(start, stop, step) — із заданим кроком.


# 8.3. Накопичення результату
total = 0
for number in range(1, 5):
    total = total + number
print(total) # 10  (0+1) + (1+1) + (2+1) + (3+1) ... =10