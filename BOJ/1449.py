n, l = map(int, input().split())
l -= 1
pipe = []
count = 0
for i in range(1001):
    pipe.append(0)
location = list(map(int, input().split()))
location.sort()
for i in location:
    pipe[i] = 1
for i in range(location[len(location)-1]+1):
    if i >= 1001:
        break
    if pipe[i] == 1:
        pipe[i] = 0
        for j in range(l+1):
            if i >= 1000:
                break
            pipe[i+j] = 0
        count += 1
print(count)
 