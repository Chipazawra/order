import random

array = [i for i in range(127)]

random.shuffle(array)

print(array)

for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


print(array)