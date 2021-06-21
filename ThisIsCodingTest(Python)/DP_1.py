n = int(input())
k = list(map(int, input().split()))
count = 0
result = []


def test(n, count):
    count += k[n]
    if n - 2 >= 0:
        test(n-2, count)
    else:
        result.append(count)


i = n - 1
while i > 0:
    test(i, 0)
    i -= 1
print(max(result))

'''
모범 답안:

n = int(input())
k = list(map(int, input().split()))
d = [0] * 100
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])
print(d[n-1])

'''
