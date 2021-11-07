t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    priority = []
    for i in range(n):
        priority.append([l[i],i])
    c = 0
    while True:
        result = 'IMPOSSIBLE_VALUE'
        if max(priority, key = lambda x : x[0]) == priority[0]:
            result = priority.pop(0)
            c += 1
        else:
            priority.append(priority.pop(0))
        if result[1] == m:
            print(c)
            break