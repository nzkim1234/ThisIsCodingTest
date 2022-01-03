a = input()
y = ord(a[0])
x = int(a[1])

move_x = [1, 1, -1, -1, 2, 2, -2, -2]
move_y = [2, -2, 2, -2, 1, -1, 1, -1]
count = 0
for i in range(len(move_y)):
    nx = x + move_x[i]
    ny = y + move_y[i]
    if nx >= 1 and nx <= 8 and ny >= ord('a') and ny <= ord('h'):
        count += 1
print(count)

'''
모범 답안:
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)

'''
