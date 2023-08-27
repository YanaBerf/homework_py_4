""" Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств."""

n = int(input('Введите длину первого множества: '))
first_set = set(input('Заполните первое множество числами: ') for i in range(n))
m = int(input('Введите длину второго множества: '))
second_set = set(input('Заполните второе множество числами: ') for i in range(m))
print(first_set)
print(second_set)
# sort_set = sorted(first_set.intersection(second_set))// через метод sorted
# print(sort_set)
intersection_sets = first_set.intersection(second_set)
print(f'пересечение множеств {intersection_sets}')
list1 = list(set(intersection_sets)) # преобразование в список
print(list1)

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)  
# sort_set = sorted(first_set.intersection(second_set))
# print(sort_set)
