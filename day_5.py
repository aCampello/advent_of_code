with open('input_5.txt', 'r') as f:
    lines = []
    max_x = 0  # So i know the gridsize
    max_y = 0
    for row in f:
        x1y1, x2y2 = row[:-1].split('->')
        x1, y1 = x1y1.split(',')
        x2, y2 = x2y2.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        lines.append([(x1, y1), (x2, y2)])


# Create empty board

# Part A

board = []

for x in range(max_x+1):
    board.append([0]*(max_y+1))

# Fills board
for (x1, y1), (x2, y2) in lines:
    if x1 == x2:
        lower_y = min(y1, y2)
        upper_y = max(y1, y2)
        for y in range(lower_y, upper_y+1):
            board[x1][y] += 1
    if y1 == y2:
        lower_x = min(x1, x2)
        upper_x = max(x1, x2)
        for x in range(lower_x, upper_x+1):
            board[x][y1] += 1

n_more_than_one_line = 0

for x in range(max_x+1):
    for y in range(max_y+1):
        if board[x][y] > 1:
            n_more_than_one_line += 1

print(n_more_than_one_line)

# Part B

board = []

for x in range(max_x+1):
    board.append([0]*(max_y+1))

# Fills board
for (x1, y1), (x2, y2) in lines:
    if x1 == x2:
        lower_y = min(y1, y2)
        upper_y = max(y1, y2)
        for y in range(lower_y, upper_y+1):
            board[x1][y] += 1
    elif y1 == y2:
        lower_x = min(x1, x2)
        upper_x = max(x1, x2)
        for x in range(lower_x, upper_x+1):
            board[x][y1] += 1
    else:
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        x_m = x1
        y_m = y1

        while (x_m, y_m) != (x2, y2):  # x_m -> x in the middle
            board[x_m][y_m] += 1
            x_m += x_step
            y_m += y_step

        board[x2][y2] += 1

n_more_than_one_line = 0

for x in range(max_x+1):
    for y in range(max_y+1):
        if board[x][y] > 1:
            n_more_than_one_line += 1

print(n_more_than_one_line)
