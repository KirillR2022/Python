# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# # (т.е. не меньше заданного минимума и не больше заданного максимума)...


import random


min_rand = 0
max_rand = 100

arr = [random.randint(0,90) for _ in range(20)]

print(arr)

for index, i in enumerate(arr):
    if 30 > i > 10:
        print (f"array[{index}] = {i} ")