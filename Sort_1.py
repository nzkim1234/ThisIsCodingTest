n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
count = 0
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
print(sum(a))


'''
모범 답안:
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))

'''
