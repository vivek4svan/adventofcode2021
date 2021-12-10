
with open('day_01_input.txt') as f:
    data_lines = map(int,f.readlines())

def solution_prob_01():
    prev_data = 0
    increase_ctr = -1

    for curr_data in data_lines:
        if prev_data < curr_data: increase_ctr += 1
        prev_data = curr_data
    return increase_ctr

def solution_prob_02():
    prev_window = 0
    increase_ctr = -1
    total_values = len(data_lines)

    for index in range(total_values):
        if index+2 < total_values:
            curr_window = data_lines[index] + data_lines[index+1] + data_lines[index+2]
        if prev_window < curr_window: increase_ctr += 1
        prev_window = curr_window
    return increase_ctr

print(solution_prob_02())