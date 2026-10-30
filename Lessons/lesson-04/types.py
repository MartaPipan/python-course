count = 12
print("Тип змінної count:", type(count)) 

text_count = "12"
print("Тип змінної text_count:", type(text_count)) #Змінна text_count містить текст, а не число.
#Хоча ми бачимо цифри 12, лапки " " говорять Python: «Це текст, який складається з символів 1 і 2».

print(12 + 3)         #15
print("12" + "3")     #123

# Автоматичне перетворення типів даних 
#Python створить результат 4.5 типу float. Перетворення 4 до сумісного числового представлення відбулося без окремого виклику з нашого боку.
#  Таке перетворення називають неявним або автоматичним.
result = 4 + 0.5
print(result)
print(type(result))    # type(float)  4.5


text_count = "14"
count = int(text_count) #Функція int() означає: «Спробуй прочитати цей текст як ціле число».

print(count)
print(type(count))
# Функція int() читає придатний запис цілого числа й повертає нове значення типу int:14<class 'int'> 




#Три базові функції перетворення

# int() створює ціле число
students = int("24")
print(students)   #24
print(type(students))  #<class 'int'>

#float() створює число з дробовою частиною
temperature = float("18.5")
print(temperature)   #18.5
print(type(temperature))  #<class 'float'>

#str() створює текстове представлення
lesson_number = 4
lesson_text = str(lesson_number)
print(lesson_text)
print(type(lesson_text))


# int() відкидає дробову частину, а round() округлює до найближчого цілого числа.
print(int(7.9))  # 7
print(int(-7.9))  # -7

print(round(7.9))  # 8
print(round(-7.9))  # -8



# list literal
fruits = ["apple", "mango", "orange"] 
print(fruits)

# tuple literal
numbers = (1, 2, 3) 
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)


x =15
y=4

print('x + y = ',x+y)
print('x - y = ',x-y) 
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)  	
print('x ** y = ',x**y) 
print('x % y = ',x%y)

print("12" + 3)  # TypeError: can only concatenate str (not "int") to str