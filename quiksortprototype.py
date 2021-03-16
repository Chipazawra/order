import random

def QuickSort(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                QuickSort(A, l, j)
                QuickSort(A, i, r)

array = [i for i in range(127)]
random.shuffle(array)
print(array)
QuickSort(array, 0, len(array) - 1)
print(array)