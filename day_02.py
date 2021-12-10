
with open('day_02_input.txt') as f:
    data_lines = f.readlines()

def solution_prob_01():
    horizontal = 0
    depth = 0

    for curr_data in data_lines:
        steer_input = curr_data.split()
        if steer_input[0] == "forward":
            horizontal += int(steer_input[1])
        elif steer_input[0] == "up":
            depth -= int(steer_input[1])
        elif steer_input[0] == "down":
            depth += int(steer_input[1])
    return horizontal*depth

def solution_prob_02():
    horizontal = 0
    depth = 0
    aim = 0

    for curr_data in data_lines:
        steer_input = curr_data.split()
        if steer_input[0] == "forward":
            horizontal += int(steer_input[1])
            depth += int(steer_input[1])*aim
        elif steer_input[0] == "up":
            aim -= int(steer_input[1])
        elif steer_input[0] == "down":
            aim += int(steer_input[1])
    return horizontal*depth

print(solution_prob_02())