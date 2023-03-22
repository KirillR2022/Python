# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
a = [randint(0,9) for i in range(int(input('Введите количество элементов: ')))]
print(a)
Flag = True
x = int(input('Введите число X: '))
count = 1
x_1 = x
while Flag:
    for i in range(len(a)):
        if a[i] == x:
            print(f'число {a[i]} самый близкий элемент к числу {x_1}')
            Flag = False
            break
    if count%2==0:
        x += count
    else:
        x -= count
    count +=1
