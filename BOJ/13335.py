from collections import deque

n, w, l = map(int, input().split())
a = deque(map(int, input().split()))
bridge = deque([0] * w)
t = 0
while a:
    t += 1
    bridge.popleft()
    if sum(bridge) + a[0] <= l:
        bridge.append(a.popleft())
    else:
        bridge.append(0)
while sum(bridge) > 0:
    t += 1
    bridge.popleft()
print(t)