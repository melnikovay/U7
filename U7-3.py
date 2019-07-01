#Массив размером 2m + 1, где m — натуральное число,
#заполнен случайным образом. Найдите в массиве медиану.
#Медианой называется элемент ряда, делящий его на две равные части:
#в одной находятся элементы, которые не меньше медианы,
#в другой — не больше медианы.
import random
MIN1 = 1
MAX1 = 100
m = int(input('Введите натуральное число' , ))
SIZE = 2 * m + 1
MASS = [random.randint(MIN1, MAX1) for _ in range (SIZE)]
print(MASS)
while len(MASS) >= 3:
    min1 = MASS.index(min(MASS))
    MASS.pop(min1)
    max1 = MASS.index(max(MASS))
    MASS.pop(max1)
    
    #print(MASS)
print('Медиана массива', MASS)    

