
from collections import defaultdict

with open('day_12_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    #main_vals = [[int(val) for val in line] for line in data_lines]
    ROWS = len(data_lines)
    COLS = len(data_lines[0])

def display_vals(inp):
    for val in inp:
        print(str(val) + " : " + str(inp[val]))
    print("_______________________")

def solution_prob_01():
    caves = defaultdict(list)
    reached = []
    for path in data_lines:
        a,b = path.split("-")
        caves[a].append(b)
        caves[b].append(a)
    display_vals(caves)
    to_visit = [[["start"],False]]
    print(to_visit)

    while len(to_visit) > 0:
        path, twice_flag = to_visit.pop()
        if path[-1] == "end":
            reached.append(path)
            continue

        for c in caves[path[-1]]:
            if c == "start": continue
            elif c.isupper() or c not in path:
                to_visit.append([path + [c],twice_flag])
            elif path.count(c) == 1 and not twice_flag:
                to_visit.append([path + [c],True])

        print(to_visit)

    #print(reached)

    print("OUTPUT : " + str(len(reached)))

def solution_prob_02():
    display_vals()
    output = 0
    print("OUTPUT : " + str(output))


solution_prob_01()
#solution_prob_02()
