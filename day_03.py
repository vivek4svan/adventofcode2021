with open('day_03_input.txt') as f:
    data_lines = f.readlines()

def solution_prob_01():
    gamma = ""
    epsilon = ""
    len_str = len(data_lines[0].strip())
    ones = [0] * len_str
    zeros = [0] * len_str

    for curr_data in data_lines:
        for index in range(len_str):
            if curr_data[index] == "0":
                zeros[index] += 1
            else:
                ones[index] += 1

    for index in range(len_str):
        if ones[index] > zeros[index]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    return int(gamma,2) * int(epsilon,2)

def solution_prob_02():
    len_str = len(data_lines[0].strip())
    oxygen = [lines.strip() for lines in data_lines]
    co2 = [lines.strip() for lines in data_lines]
    ones = [0] * len_str
    zeros = [0] * len_str

    for index in range(len_str):
        for data in oxygen:
            if data[index] == "0":
                zeros[index] += 1
            else:
                ones[index] += 1
        if ones[index] >= zeros[index]:
            oxygen = [x for x in oxygen if x[index] == "1"]
        else:
            oxygen = [x for x in oxygen if x[index] == "0"]
        if len(oxygen) == 1: break

    ones = [0] * len_str
    zeros = [0] * len_str

    for index in range(len_str):
        for data in co2:
            if data[index] == "0":
                zeros[index] += 1
            else:
                ones[index] += 1
        if ones[index] < zeros[index]:
            co2 = [x for x in co2 if x[index] == "1"]
        else:
            co2 = [x for x in co2 if x[index] == "0"]
        if len(co2) == 1: break

    return int(oxygen[0],2) * int(co2[0],2)

print(solution_prob_01())
print(solution_prob_02())