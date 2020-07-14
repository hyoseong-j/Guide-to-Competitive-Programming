N = int(input())
array = [1, 3, 8, 2, 9, 2, 5, 6]
for i in range(0, N):
    for j in range(0, N - 1):
        print(array)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


