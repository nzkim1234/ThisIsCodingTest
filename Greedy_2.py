num = input()
result = int(num[0])
for i in range(1,len(num)):
    if result == 0:
        result += int(num[i])
    elif int(num[i]) > 1:
        result *= int(num[i])
    else:
        result += int(num[i])
print(result)

'''
모범 답안:

data = input()
result = int(data[0])
for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

'''