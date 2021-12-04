from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
graph[0][0] = 1
movement = deque()
time = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction_index = 0
snake_head = [0, 0]
snake_body = deque()


for k in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    graph[x-1][y-1] = 2


for l in range(int(stdin.readline())):
    switch_time, rotate = stdin.readline().split()
    movement.append([int(switch_time), rotate])

switch_time, change_direction = movement.popleft()

while True:

    if switch_time == time:
        if change_direction == 'D':
            direction_index += 1
            
            if direction_index > 3:
                direction_index = 0
        else:
            direction_index -= 1
            
            if direction_index < 0:
                direction_index = 3

        if movement:
            switch_time, change_direction = movement.popleft()

    x, y = snake_head
    n_x = x + direction[direction_index][0]
    n_y = y + direction[direction_index][1]

    if 0 <= n_x < n and 0 <= n_y < n and graph[n_x][n_y] != 1:
        snake_body.append(snake_head)
        snake_head = [n_x, n_y]
        if graph[n_x][n_y] != 2:
            r_x, r_y = snake_body.popleft()
            graph[r_x][r_y] = 0
        graph[n_x][n_y] = 1
    else:
        break
    
    time += 1

print(time + 1)