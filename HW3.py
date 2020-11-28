# Задание №2
# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = int(input("Введите число "))
new_value = value/2 if value < 100  else -value
print(new_value)

###############################################################################
# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
value = int(input("Введите число "))
new_value = 1 if value < 100 else 0
print(new_value)

###############################################################################
# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False
value = int(input("Введите число "))
new_value = True if value < 100 else False
print(new_value)

##############################################################################
#4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
my_str = 'HeLlO,,,  wOrLd!'
high_str = my_str.upper()
print(high_str)

##############################################################################
# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
my_str = 'HeLlO,,,  wOrLd!'
low_str = my_str.lower()
print(low_str)

##############################################################################
# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str = input("Напишите текст: ")
len_str = len(my_str)
my_str = my_str*2 if len_str < 5 else my_str
print(my_str)

##############################################################################
# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str = input("Напишите текст: ")
len_str = len(my_str)
str_my = my_str[::-1]
my_str = str_my if len_str <5 else my_str
print(my_str)

##############################################################################
# 8) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.
my_str = 'HeLlO,,,  wOrLd!'
for symbol in my_str:
    if symbol.isalnum():
        print(symbol)

##############################################################################
# 9) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.
my_str = 'HeLlO,,,  wOrLd!'
for symbol in my_str:
     if not symbol.isalnum():
         print(symbol)

##############################################################################
# 10) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.
my_str = 'HeLlO,,,  wOrLd!'
for symbol in my_str:
      if not symbol.isalnum() and not symbol == " ":
          print(symbol)
