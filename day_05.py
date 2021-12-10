with open('day_05_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    len_data = len(data_lines)
    master_list = []
    for i in range(1000):
        master_list.append([0]*1000)

def display_lines(lines):
    for line in lines:
        print(line)

def display_master_list():
    for lst in master_list:
        print("")
        for column in lst:
            print(column),

def solution_prob_01():
    ctr = 0
    line_vals = []
    for data in data_lines:
        temp = data.split(" -> ")
        x1,y1 = [int(val) for val in temp[0].split(",")]
        x2,y2 = [int(val) for val in temp[1].split(",")]
        if x1 == x2 or y1 == y2:
            line_vals.append([(x1,y1),(x2,y2)])
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    print(x,y)
                    master_list[y][x] += 1
                    if master_list[y][x] == 2:
                        ctr += 1
    #display_lines(line_vals)
    #display_master_list()
    print("\n\nOUTPUT : " + str(ctr))

def solution_prob_02():
    ctr = 0
    line_vals = []
    for data in data_lines:
        temp = data.split(" -> ")
        x1,y1 = [int(val) for val in temp[0].split(",")]
        x2,y2 = [int(val) for val in temp[1].split(",")]
        if x1 == x2 or y1 == y2:
            line_vals.append([(x1,y1),(x2,y2)])
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    #print(x,y)
                    master_list[y][x] += 1
                    if master_list[y][x] == 2:
                        ctr += 1
            #display_master_list()
            print("STRAIGHT : " + str(ctr))
        elif abs(x1 - x2) == abs(y1 - y2):
            line_vals.append([(x1,y1),(x2,y2)])
            x = x1
            y = y1
            for _ in range(min(x1,x2),max(x1,x2)+1):
                #print(x,y)
                master_list[y][x] += 1
                if master_list[y][x] == 2:
                    ctr += 1
                if x1 > x2: x = x - 1
                else: x = x + 1
                if y1 > y2: y = y - 1
                else: y = y + 1
                
            #display_master_list()
            print("DIAGONAL : " + str(ctr))

    #display_lines(line_vals)
    #display_master_list()
    print("\n\nOUTPUT : " + str(ctr))

#solution_prob_01()
solution_prob_02()