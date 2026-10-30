x =15
y=4

print('x + y = ',x+y)
print('x - y = ',x-y) 
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)  	
print('x ** y = ',x**y) 
print('x % y = ',x%y)


x = 10
y = 12
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)


x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)



#Example: < and <=
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x < y)
print(f"x < y ---> {result}")

result = (x <= y)
print(f"x <= y ---> {result}")

result = (x < 10)
print(f"x < 10 ---> {result}")

result = (x <= 10)
print(f"x <= 10 ---> {result}")

#Example: == and !=
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x == y)
print(f"x == y ---> {result}")

result = (x != y)
print(f"x != y ---> {result}")

result = (x == 10)
print(f"x == 10 ---> {result}")

result = (x != 10)
print(f"x != 10 ---> {result}")

name1 = "Alice"

print(name1 == "Alice")   # True
print(name1 == "alice")   # False
print(name1 != "Alice")   # False
print(name1 != "alice")   # True



#The not operator reverses a boolean (or boolean expression). If age >= 18 is True, then not (age >= 18) is False.
passcode = "1345"
entered_code = input("Enter passcode: ")
result = (passcode == entered_code)
print(f"Is passcode equal to entered code? {result}")

result = not (passcode == entered_code)
print(f"Is passcode not equal to entered code? {result}")

print(bool(1))
print(bool(10))
print(bool(-5))
print(bool(0)) #false
print(bool("Hello"))
print(bool("Python"))
print(bool("")) #false
print(bool([1, 2, 3])) #true
print(bool([])) #false
bool(0)       # False
bool("")      # False
bool([])      # False
bool(None)    # False
bool(5)       # True
bool("Hi")    # True
bool([1, 2])  # True



print("2026", "09", "01", sep="-")    #2026-09-01

print("Завантаження", end="...")  #Завантаження...
print("готово!")                  #готово!           
 #результат буде в одному рядку: Завантаження...готово