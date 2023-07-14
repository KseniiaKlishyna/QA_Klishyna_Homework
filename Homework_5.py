import numpy as np
#1 Знаходження перетину двох заданих масивів за допомогою лямбда.

array_1 = np.array([33, 456, 0, 4, -596, 33333])
array_2 = np.array([0, 78, -596, 234])

array_3 = lambda x, y: np.intersect1d(x,y)

print(array_3(array_1, array_2))

#2 чи є заданий рядок числом, за допомогою лямбда

check = lambda x: x.isnumeric()
print(check("2893944"))

#3 Знайти список із максимальною та мінімальною довжиною за допомогою лямбда.

list_1 = [1, 2, 3, 4, 6788]
list_2 = [0,1,2]
list_3 = [5]
list_4 = [1,2,3,4,5,6,7,8]
general_list = [list_1] + [list_2] + [list_3] + [list_4]
min_len = lambda x: min(x, key=len)
max_len = lambda x: max(x, key=len)
print(min_len(general_list), max_len(general_list))
