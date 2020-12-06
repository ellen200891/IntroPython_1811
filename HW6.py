# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['qwe', '123', 'zxc', '456', 'asd', '789']
new_list = []
for id,item in enumerate(my_list):
    if id % 2 != 0:
        item = str(my_list[id])
        item = item[::-1]
        new_list.append(item)
    else:
        new_list.append(my_list[id])
print(new_list)

#############################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".


my_list = ['qwe', '123', 'zxc', '456', 'asd', '789']
first_a = []
first_a = [element for element in my_list if element[0] == 'a']
print(first_a)


#############################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['qwe', '123', 'zxc', '456', 'asd','lka', '789', 'jha']
sub = 'a'
new_list = []
for text in my_list:
    if sub in text:
        new_list.append(text)
print(new_list)


#############################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['qwe', '123', 'zxc', 1, 3, 5, '456', 'asd', 'lka', 5, 6, '789', 'jha', 'dkfjgl']
new_list = []
for text in my_list:
    if type(text) == str:
        new_list.append(text)
print(new_list)

#############################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = '1234567899876543210asdkdsa'
set_str = set(my_str)
new_str = ([x for x in set_str if my_str.count(x) == 1])
print(new_str)

#############################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

first_str = '12345678k998765kkk43210asddsa'
second_str = 'kjkjlk jkljkj jklkj1'
for element in first_str:
  for element in second_str:
   new_str = set(first_str).intersection(set(second_str))
print(list(new_str))

#############################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

first_str = '1234567r8j99'
first_set =set(first_str)
second_str = 'jlkjlkjrlj1999'
second_set =set(second_str)
new_str_1 = set([x for x in first_set if first_str.count(x) == 1])
new_str_2 = set([x for x in second_set if second_str.count(x) == 1])
for i in new_str_1:
  for i in new_str_2:
        new_str = new_str_1.intersection(new_str_2)
print(list(new_str))

#############################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
adress = {"country":"USA",
          "city":"LA",
          "street":"Sunset"}
job = {"have":"Yes",
       "position":"singer"}
person = {
    "s_name":"Jackson",
    "name":"Michael ",
    "age":"50",
    "adress":adress,
    "job":job
}
print(person)

#############################################################################

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
cakes = {"flour":"400g",
         "milk":"1l",
         "butter":"100g",
         "eggs":"5 items"}
cream = {"sugar":"300g",
         "bread":"50g",
         "vanilla":"2g",
         "sour_cream": "500g"}
glaze = {"cacao":"150g",
         "sugar":"300g",
         "bread":"100g"}
components = {"cakes":cakes,
              "cream":cream,
              "glaze":glaze}
print(components)
