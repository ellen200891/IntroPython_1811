# параметры функций
# *arg, **kwargs
# работа с фаилами
# time,sys, os, os.path
# import random
# import string
import os


with open("C:/Users/Пользователь/Desktop/Hillel1/lesson7.txt","r", encoding="utf-8") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())

print(len(data), type(data))
for line in data:
    print(line)

with open("C:/Users/Пользователь/Desktop/Hillel1/lesson7.txt", "w") as txt_file:
    txt_file.write("\n".join(data))




# print(string.ascii_lowercase)
# DEBUG_MOD = True
#
# def create_random_str(str_len, debug_mod=False):
#     alphabet = list(string.ascii_lowercase)
#     random.shuffle(alphabet)
#     random_str = "".join(alphabet[:str_len])
#     if debug_mod:
#         print(random_str)
#     return random_str
#
# def testing_args(q, w, e, r, t, y, debug_mod=DEBUG_MOD):
#     if debug_mod:
#         print(q, w, e, r, t, y)
# random_str = create_random_str(10, debug_mod=DEBUG_MOD)
#
# testing_args = (1,2,3,4,5,6)



# def testing_args(q, w, e, r, t, y):
#     print(q, w, e, r, t, y)
#
# def testing_default_values(first, second):
#     result = first + second
#     return result
#
# result = testing_default_values(12, 10)
# print(result)



#testing_args("q", "w", r=1, y=2, t=0, e="e")





# def crate_random_point(min_limit, max_limit):
#     # print("min_limit", "max_limit", min_limit, max_limit)
#     point = (random.randint(min_limit, max_limit),
#              random.randint(min_limit, max_limit),
#              random.randint(min_limit, max_limit))
#     return point
#
#
# def crate_line_segment(stop, start):
#     line_segment = {"A": crate_random_point(start, stop),
#                     "B": crate_random_point(start, stop)}
#     return line_segment


# point_max = crate_random_point(-100, 100)
# point = crate_random_point(-10, 10)

# print(point_max)

# AB = crate_line_segment(10, 100)   ######### Позиционные аргументы #######
# print(AB)
# stop = 100
# start = 10
# AB = crate_line_segment(stop=stop, start=start)  # именованные аргументы
# print(AB)
