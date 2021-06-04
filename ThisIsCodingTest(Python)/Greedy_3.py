n = int(input())
p = list(map(int, input().split()))
p.sort()
count = 0
result = 0
for i in range(n):
    count += 1
    if count >= p[i]:
        result += 1
        count = 0
print(result)


'''
모범 답안:
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

'''