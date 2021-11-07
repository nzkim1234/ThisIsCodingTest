n = int(input())
money = list(map(int, input().split()))
m = int(input())
if sum(money) <= m:
    print(max(money))
else:
    s = 1
    e = m
    while s < e:
        total_price = 0
        mid = (s+e) // 2
        for i in money:
            if i > mid:
                total_price += mid
            else:
                total_price += i
        if total_price > m:
            e = mid - 1
        else:
            s = mid + 1
    total_price = 0
    for i in money:
        if i > e:
            total_price += e
        else:
            total_price += i
    if total_price > m:
        e -= 1
    print(e)