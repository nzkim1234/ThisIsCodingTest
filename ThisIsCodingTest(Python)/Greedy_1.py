n, k = int(input().split())
count = 0
while n > 1:
    if n // k > 0:
        count += 1
        n = n // k
    else:
        count += 1
        n -= 1
print(count)

'''
모범 답안:
n, k = map(int, input().split())
result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)

'''