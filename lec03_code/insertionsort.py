import numpy as np

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key
    return L

if __name__ == "__main__":
    L = np.random.randint(100, size=10)
    insertion_sort(L)
    print(L)