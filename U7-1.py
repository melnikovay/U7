#Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100).
#Выведите на экран исходный и отсортированный массивы.

import random
MIN1 = -100
MAX1 = 100
SIZE = 10
MASS = [random.randint(MIN1, MAX1) for _ in range (SIZE)]

print('Исходный массив' , MASS)

def sort_p(MASS):
    n = 1
    while n < len(MASS):
         for i in range(len(MASS) - 1):
           if MASS[i] > MASS[i+1]:
               MASS[i],MASS[i+1] = MASS[i+1],MASS[i]
               p = 1
               print(MASS)
         if p != 1:
             break
         
         n +=1
    return(MASS)
print('Отсортированный массив', sort_p(MASS))
    

