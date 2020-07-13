# O(n**3) 시간 풀이

a = [-1, 2, 4, -3, 5, 2, -5, 2]

N = int(input())
best = 0

for i in range(0, N):
    for j in range(i, N):
        sum = 0
        for k in range(i, j + 1):
            sum += a[k]
        best = max(best, sum)
print(best)

# O(n**2) 시간 풀이

a = [-1, 2, 4, -3, 5, 2, -5, 2]

N = int(input())
best = 0
for i in range(0, N):
    sum = 0
    for j in (i, N):
        sum += a[j]
        best = max(best, sum)
print(best)


# O(n) 시간 풀이

a = [-1, 2, 4, -4, 5, 2, -5, 2]

N = int(input())
best = 0
sum = 0
for i in range(0, N):
    sum = max(a[i], sum + a[i])
    best = max(best, sum)
print(best)
