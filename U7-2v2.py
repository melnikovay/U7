#Отсортируйте по возрастанию методом слияния одномерный вещественный
#массив, заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.
import random
MIN1 = 0
MAX1 = 50
SIZE = 10
MASS = [random.randint(MIN1, MAX1) for _ in range (SIZE)]
print(MASS)

def sort_mass (MASS1, MASS2):
    sort_mass = []
    MASS1_id = MASS2_id = 0
    MASS1_len, MASS2_len = len(MASS1), len(MASS2)
    for _ in range (MASS1_len + MASS2_len):
        if MASS1_id < MASS1_len and MASS2_id < MASS2_len:
            if MASS1[MASS1_id] <= MASS2[MASS2_id]:
               sort_mass.append(MASS1[MASS1_id])
               MASS1_id+=1
            else:
               sort_mass.append(MASS2[MASS2_id])
               MASS2_id+=1  
        elif MASS1_id == MASS1_len:
           sort_mass.append(MASS2[MASS2_id])
           MASS2_id+=1
        elif MASS2_id == MASS2_len:
           sort_mass.append(MASS1[MASS1_id])
           MASS1_id+=1
    #print (MASS1)
   # print (MASS2)
    #print (sort_mass)
    return sort_mass        


def del_mass (MASS):
    if len(MASS) <= 1:
        return MASS
    d = len(MASS)//2
    MASS1 = del_mass(MASS[: d])
    MASS2 = del_mass(MASS[d :])
   # print (MASS1, MASS2)
    return sort_mass(MASS1, MASS2)

MASS_sort = del_mass (MASS)
print (MASS_sort)
