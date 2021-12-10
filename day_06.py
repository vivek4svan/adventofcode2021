from collections import defaultdict


with open('day_06_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    master_list = [int(val) for val in data_lines[0].split(",")]

def solution_prob_01():
    itr = 0
    while itr < 80:
        len_data = len(master_list)
        for i in range(len_data):
            if master_list[i] != 0:
                master_list[i] = master_list[i] - 1
            elif master_list[i] == 0:
                master_list[i] = 6
                master_list.append(8)
        itr += 1
        #print(str(itr) + " : " + str(master_list))
        print("OUTPUT : " + str(itr) + " : " + str(len(master_list)))

def solution_prob_02():
    itr = 0
    data_dict = defaultdict(int)
    for val in master_list:
        if val not in data_dict: data_dict[val] = 1
        else: data_dict[val] += 1

    while itr < 256:
        #print(data_dict)
        new_dict = defaultdict(int)
        for key,val in data_dict.items():
            if key == 0:
                new_dict[6] += val
                new_dict[8] += val
            else:
                new_dict[key-1] += val
        itr += 1
        data_dict = new_dict
        print(str(itr) + " : " + str(data_dict))
        print("OUTPUT : " + str(itr) + " : " + str(sum(data_dict.values())))

#solution_prob_01()
solution_prob_02()