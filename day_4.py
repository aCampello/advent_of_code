
boards = []

with open('input_4.txt', 'r') as f:
    numbers = [int(n) for n in f.readline().rstrip('\n').split(',')]

    while f.readline():
        current_board = []
        for _ in range(5):
            current_board.append([int(n) for n in f.readline().rstrip('\n').split(' ') if n])

        boards.append(current_board)

# Part A

# boards[i,j,k] is board i, row j, column k
def board_won(board, drawn_numbers):
    for j in range(5):
        if sum([board[j][k] in drawn_numbers for k in range(5)]) == 5 or \
                sum([board[k][j] in drawn_numbers for k in range(5)]) == 5:
            return True

    return False


# Loops to check if board won
winning_board = None
winning_numbers = None

for n_i in range(1, len(numbers)):
    drawn_numbers = numbers[:n_i]

    for board in boards:
        if board_won(board, drawn_numbers):
            winning_board = board
            winning_numbers = drawn_numbers

    if winning_board:
        break

# Compute final result

non_marked_numbers = sum([n for row in winning_board for n in row if n not in drawn_numbers])
print(non_marked_numbers*drawn_numbers[-1])

# Part B

winning_boards = 0
boards_in_play = boards
n_i = 0

boards_that_won = []
last_board = []

for n_i in range(1, len(numbers)):
    drawn_numbers = numbers[:n_i]

    boards_that_won_this_round = []
    for i, board in enumerate(boards_in_play):
        if board_won(board, drawn_numbers):
            if i not in boards_that_won:
                boards_that_won.append(i)
                winning_boards += 1
                if winning_boards == len(boards):
                    last_board = board
                    last_numbers = drawn_numbers

    if last_board:
        break

non_marked_numbers = sum([n for row in last_board for n in row if n not in drawn_numbers])
print(non_marked_numbers*drawn_numbers[-1])





