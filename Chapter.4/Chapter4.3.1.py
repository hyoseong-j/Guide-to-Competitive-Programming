#이진탐색(binary search)

array = [1,3,3, 4, 5, 5,6, 9, 10, 12, 12, 15]
n = len(array)


a = 0
b = n - 1
x = int(input())
while a <= b:
    k = (a + b) // 2
    if array[k] == x:
        print(array[k])
    if array[k] < x:    a = k + 1
    else:   b = k - 1


