# 1. Дано целое число (int). Определить сколько нулей в этом числе.


value = input('Введите число: ')
value_str = str(value)
count = value.count('0')
print(count)

############################################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.


value = input('Введите число: ')
len_value = len(value)
zero = len(value.rstrip('0'))
count = len_value - zero
print(count)

############################################################################
# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.


my_list_1 = [10, 20, 30, 40, 50, 60,70,80]
my_list_2 = [1, 2, 3, 4, 5, 6]
my_result = []
for index in range(len(my_list_1)):
    if not index %2:
        my_result.append(my_list_1[index])
for index in range(len(my_list_2)):
    if index %2 != 0:
        my_result.append(my_list_2[index])
print(my_result)


############################################################################
# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]

my_list_1 = [10, 21, 31, 40, 53, 65,74,80]
my_list_2 = [1, 2, 3, 4, 5, 6]
my_result = []
for number in my_list_1:
    if not number %2:
        my_result.append(number)
for number in my_list_2:
    if number % 2 != 0:
        my_result.append(number)
print(my_result)


############################################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]


my_list = [1, 10, 21, 31, 40, 53, 65, 74, 80]
new_list = []
new_list.extend(my_list[1:])
new_list.append(my_list[0])
print(new_list)

############################################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 10, 21, 31, 40, 53, 65, 74, 80]
my_list.append(my_list.pop(0))
print(my_list)

############################################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

my_str = '43 34 56 hjghj 1'
word_list = my_str.split()
num_list = []
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
        sum_list = sum(num_list)
print(sum_list)

############################################################################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']


my_str = 'abcнd'
new_str = []
for i in range(0, len(my_str), 2):
    if len(my_str)%2 != 0:
        my_str = my_str + '_'
    new_str.extend([my_str[i:i + 2]])
print(new_str)

############################################################################


# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"


my_str = "My_long str"
l_limit = 'o'
r_limit = 't'
start = my_str.index(l_limit)
finish = my_str.index(r_limit)
sub_str = my_str[start+1:finish]
print(sub_str)

############################################################################


# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
start = my_str.index(l_limit)
finish = my_str.rfind(r_limit)
sub_str = my_str[start+1:finish]
print(sub_str)


############################################################################


# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.


my_list = [2, 4, 1, 5, 3, 9, 0, 7]
sum_number = 0
for number in range(1, len(my_list) - 1):
    if my_list[number - 1] < my_list[number] > my_list[number + 1]:
        sum_number += 1
print(sum_number)