#Ім'я — це назва, яку ми даємо об'єкту, щоб потім звертатися до нього.
#Літерал — це спосіб записати конкретне значення безпосередньо в коді.

pages_read = 4
print(pages_read)

pages_read = 4
print("Прочитано сторінок:", pages_read)
pages_read = 5
print("Після наступної сторінки:", pages_read)


lesson_number = 3       #є цілим числом -int
temperature = 18.5      #є числом з плаваючою комою -float
student_name = "Олена"  #є рядком       -str
city = 'Львів'


#    True та False єлогічними значеннями,
#    None позначає відсутність звичайного значення в певному місці програми

lesson_number = 3
student_name = "Олена"
print(type(lesson_number))
print(type(student_name))

print(type(lesson_number))
print(type(student_name))


#Ім’я, яким у коді позначають змінну, функцію або інший програмний об’єкт, називається ідентифікатором
#1. використовуйте латинські літери, цифри та нижнє підкреслення _;
#2. не поч. ім’я з цифри;
#3. не вст. пробіли або дефіси;
#4. не використовуй ключове слово Python як ім’я;
#5. великі й малі літери розрізняються.



#ключовi слова
# Не потрібно зубрити повний список ключових слів.Його можна отримати від самого Python: --->> in console((true or false))
import keyword
print(keyword.iskeyword("class"))
print(keyword.iskeyword("student_class"))


room = 201
print(room)
room = 305
print(room)

# 2course = "Python"     / не поч ім’я з цифри  /
# student name = "Ivan"  / не вставл пробіли 
# class = "КН-11"        / ключовe словo class не можна використовувати як ім’я змінної /


course_2 = "Python"
student_name = "Іvan"
class_name = "КН-11"

#Python дозволяє створити кілька зв’язків в одному рядку:
course, lesson = "Python", 3

#Ім’я великими літерами повідомляє читачеві: це константа за домовленістю, тобто значення, яке код не повинен перепризначати. 
MINUTES_IN_HOUR = 60

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