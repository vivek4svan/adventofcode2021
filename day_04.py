with open('day_04_input.txt') as f:
    data_lines = f.readlines()
    len_data = len(data_lines)
    random_num = [int(val) for val in data_lines[0].strip().split(",")]
    i = 2
    boards = []
    sub_boards = []
    while i < len_data:
        if data_lines[i] == "\n":
            boards.append(sub_boards)
            sub_boards = []
            i += 1
            continue
        sub_boards.append([int(val) for val in data_lines[i].strip().split()])
        i += 1
    boards.append(sub_boards)

def display_board():
    for board in boards:
        print("\n")
        for row in board:
            print(row)

def check_status():
    for i_board in range(len(boards)):
        for i in range(5):
            horizontal = 0
            vertical = 0
            for j in range(5):
                if boards[i_board][i][j] == -1:
                    horizontal += 1
                if boards[i_board][j][i] == -1:
                    vertical += 1
                if horizontal == 5 or vertical == 5:
                    return [boards[i_board],i_board]

def check_status2():
    remove_list = []
    for i_board in range(len(boards)):
        for i in range(5):
            horizontal = 0
            vertical = 0
            for j in range(5):
                if boards[i_board][i][j] == -1:
                    horizontal += 1
                if boards[i_board][j][i] == -1:
                    vertical += 1
                if horizontal == 5 or vertical == 5:
                    if len(boards) != 1:
                        remove_list.append(i_board)
    return set(remove_list)

def update_board(val):
    for i_board in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[i_board][i][j] == val:
                    boards[i_board][i][j] = -1

def calculate_result(board):
    sum_val = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                sum_val += board[i][j]
    print("SUM of Values : " + str(sum_val))
    return sum_val

def solution_prob_01():
    for val in random_num:
        print("Calling Number : "+str(val))
        update_board(val)
        status = check_status()
        if status is not None:
            status = status[0]
            display_board()
            print("\nSUCCESS BOARD\n")
            print(status)
            output = calculate_result(status) * val
            return output

def solution_prob_02():
    for val in random_num:
        print("Calling Number : " + str(val))
        update_board(val)
        status = check_status2()
        global boards
        if len(boards) == 1:
            print("\nSUCCESS BOARD\n")
            print(boards)
            output = calculate_result(boards[0]) * val
            return output
        boards = [i for j, i in enumerate(boards) if j not in status]

#print(solution_prob_01())
print(solution_prob_02())