#배열의 모든 원소가 유일한지 검사
array = [1, 2, 3, 5, 6, 8, 8]
a = True

for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if(array[i] == array[j]):
            a = False
print(a)
