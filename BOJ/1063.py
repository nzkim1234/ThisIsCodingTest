from sys import getrecursionlimit, stdin

king, stone, n = stdin.readline().split()
king_x, king_y = king
stone_x, stone_y = stone
chess_board = [[0 for _ in range(8)] for _ in range(8)]
king_loc = [int(king_y) - 1, ord(king_x) - 65]
stone_loc = [int(stone_y) - 1, ord(stone_x) - 65]
move_loc = []
movement = []

for _ in range(int(n)):
    movement.append(stdin.readline().strip())

for move in movement:
    new_king_loc = []
    new_stone_loc = []

    if move == 'R':
        move_loc = [0, 1]
    elif move == 'L':
        move_loc = [0, -1]
    elif move == 'B':
        move_loc = [-1 , 0]
    elif move == 'T':
        move_loc = [1, 0]
    elif move == 'RT':
        move_loc = [1, 1]
    elif move == 'LT':
        move_loc = [1, -1]
    elif move == 'RB':
        move_loc = [-1, 1]
    elif move == 'LB':
        move_loc = [-1, -1]
        
    new_king_loc = [king_loc[0] + move_loc[0], king_loc[1] + move_loc[1]]

    if 0 <= new_king_loc[0] < 8 and 0 <= new_king_loc[1] < 8:
        if new_king_loc[0] == stone_loc[0] and new_king_loc[1] == stone_loc[1]:
            new_stone_loc = [stone_loc[0] + move_loc[0], stone_loc[1] + move_loc[1]]
            
            if 0 <= new_stone_loc[0] < 8 and 0 <= new_stone_loc[1] < 8:
                king_loc = new_king_loc
                stone_loc = new_stone_loc
        else:
            king_loc = new_king_loc
    
king = chr(king_loc[1] + 65) + str(king_loc[0] + 1)
stone = chr(stone_loc[1] + 65) + str(stone_loc[0] + 1)
print(king)
print(stone)
