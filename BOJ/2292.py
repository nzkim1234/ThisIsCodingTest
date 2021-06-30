n = int(input())
start = 1
count = 1
while n > start:
    count += 1
    start += 6*count
print(count)
