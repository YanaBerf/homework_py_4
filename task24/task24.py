"""В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9 
"""
n = int(input('введите количество кустов: '))
list_n =[]
for i in range(1, n+1):
    list_n.append(i)
print(list_n)
a = int(input('введите номер куста: '))

for i in range(0, len(list_n)-1):
            if a == len(list_n):
                sum1 = list_n[-1] + list_n[-2] + list_n[0]
            else:            
                sum1 = list_n[a] + list_n[a - 1] + list_n[a - 2]
print(sum1)

"""
for i in range(len(list_n)-1):
    max_sum = 0
    sum = 0
    sum = list_n[i] + list_n[i -  1] + list_n[i + 1]
    if sum > max_sum:
        max_sum = sum
print(max_sum)
"""

