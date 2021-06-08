s = input()
alpha = []
num = 0
for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)
alpha.sort()
if num != 0:
    print(''.join(alpha) + str(num))
else:
    print(''.join(alpha))

'''
모범 답안:
data = input()
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print(''.join(result))

 '''
