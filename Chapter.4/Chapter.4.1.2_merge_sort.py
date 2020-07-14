array = [1, 3, 8, 2, 9, 2, 5, 6, -1, 0, 12, 15]
N = len(array)
for i in range(0, N):
    for j in range(0, N):
        print(array)
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]