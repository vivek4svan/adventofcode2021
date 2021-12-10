with open('day_07_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    data_lines = [int(val) for val in data_lines[0].split(",")]
    data_lines.sort()
    data_len = len(data_lines)
    print(data_lines)

def solution_prob_01():
    if data_len % 2 == 0:
        median1 = data_lines[data_len//2]
        median2 = data_lines[data_len//2 - 1]
        median = (median1 + median2)/2
    else:
        median = data_lines[data_len//2]
    print(median)
    moves = 0
    for crab in data_lines:
        moves += abs(crab - median)
    print(moves)

def calc_moves(steps):
    moves = 0
    for i in range(1,steps+1):
        moves += i
    return moves

def solution_prob_02():
    get_sum = sum(data_lines)
    mean = get_sum / data_len
    print(mean)
    moves = []
    for i in range(3):
        moves.append(0)
        for crab in data_lines:
            steps = abs(crab - mean)
            moves[i] += calc_moves(steps)
        mean += 1
    print(moves)
    print(min(moves))

#solution_prob_01()
solution_prob_02()
