
from collections import defaultdict

with open('day_13_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    #main_vals = [[int(val) for val in line] for line in data_lines]
    #ROWS = len(data_lines)
    #COLS = len(data_lines[0])
    ROWS = 0
    COLS = 0
    matrix = []

def display_vals(inp):
    for val in inp:
        #print(str(val) + " : " + str(inp[val]))
        print(val)

def display_matrix():
    print("______________________________________________________")
    for i in range(len(matrix)):
        print(matrix[i])

def solution_prob_01():
    #display_vals(data_lines)
    output = 0
    instructions = []
    points = []
    global COLS,ROWS,matrix
    for i in range(len(data_lines)):
        if "fold" in data_lines[i]:
            ins = (data_lines[i].split()[2])
            instructions.append(ins.split("="))
        elif len(data_lines[i]) > 0:
            p = map(int,data_lines[i].split(","))
            points.append(p)
            if p[0] > COLS: COLS = p[0]
            if p[1] > ROWS: ROWS = p[1]
    for i in range(ROWS+1):
        matrix.append([])
        for j in range(COLS+1):
            matrix[i].append(".")
    for p in points:
        #print(p)
        matrix[p[1]][p[0]] = "#"
    #display_vals(points)
    #display_vals(instructions)
    display_matrix()
    while len(instructions) > 0:
        stars = 0
        print("______________________________________________________")
        ins = instructions.pop(0)
        if ins[0] == "x":
            print("Processing : " + str(ins))
            ctr = 1
            fold = int(ins[1])
            for i in range(fold+1,COLS+1):
                for x in range(ROWS+1):
                    if matrix[x][i] == "#" or matrix[x][fold-ctr] == "#":
                        matrix[x][fold-ctr] = "#"
                        stars += 1
                ctr += 1
            for row in range(ROWS+1): matrix[row] = matrix[row][0:fold]
            COLS = fold - 1
            #display_matrix()
        elif ins[0] == "y":
            print("Processing : " + str(ins))
            ctr = 1
            fold = int(ins[1])
            for i in range(fold+1,ROWS+1):
                #print(matrix[i])
                for x in range(COLS+1):
                    if matrix[i][x] == "#" or matrix[fold-ctr][x] == "#":
                        matrix[fold-ctr][x] = "#"
                        stars += 1
                ctr += 1
            matrix = matrix[0:fold]
            ROWS = fold - 1
            #display_matrix()
        print("OUTPUT : " + str(stars))
    display_matrix()

def solution_prob_02():
    display_vals()
    output = 0
    print("OUTPUT : " + str(output))


solution_prob_01()
#solution_prob_02()
