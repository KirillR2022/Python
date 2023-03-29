# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint

length1 = int(input("Введите длину 1 списка: "))
my_list1 = [randint(1, 10) for i in range(length1)]

length2 = int(input("Введите длину 1 списка: "))
my_list2 = [randint(1, 10) for i in range(length2)]

print(my_list1)
print(my_list2)

print(sorted(list(set(my_list1).intersection(set(my_list2)))))