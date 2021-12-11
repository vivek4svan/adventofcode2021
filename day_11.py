
with open('day_11_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    main_vals = [[int(val) for val in line] for line in data_lines]
    ROWS = len(data_lines)
    COLS = len(data_lines[0])

def display_vals():
    for val in main_vals:
        print(val)

def solution_prob_01():
    display_vals()
    output = 0
    steps = 0
    while output != 100:
        print("----------------------------------------")
        flashed = []
        to_flash = []
        for i in range(ROWS):
            for j in range(COLS):
                val = main_vals[i][j]
                if val != 9: main_vals[i][j] += 1
                else: to_flash.append((i,j))
        #display_vals()
        print(to_flash)
        while len(to_flash) > 0:
            loc = to_flash.pop(0)
            i = loc[0]
            j = loc[1]
            flashed.append((i,j))
            main_vals[i][j] = 0
            #LEFT
            if j-1 >= 0 and (i,j-1) not in flashed:
                if main_vals[i][j-1] != 9: main_vals[i][j-1] += 1
                elif (i,j-1) not in to_flash: to_flash.append((i,j-1))
            #RIGHT
            if j+1 < COLS and (i,j+1) not in flashed:
                if main_vals[i][j+1] != 9: main_vals[i][j+1] += 1
                elif (i,j+1) not in to_flash: to_flash.append((i,j+1))
            #UP
            if i-1 >= 0 and (i-1,j) not in flashed:
                if main_vals[i-1][j] != 9: main_vals[i-1][j] += 1
                elif (i-1,j) not in to_flash: to_flash.append((i-1,j))
            #DOWN
            if i+1 < ROWS and (i+1,j) not in flashed:
                if main_vals[i+1][j] != 9: main_vals[i+1][j] += 1
                elif (i+1,j) not in to_flash: to_flash.append((i+1,j))
            #LEFT-UP
            if j-1 >= 0 and i-1 >= 0 and (i-1,j-1) not in flashed:
                if main_vals[i-1][j-1] != 9: main_vals[i-1][j-1] += 1
                elif (i-1,j-1) not in to_flash: to_flash.append((i-1,j-1))
            #RIGHT-UP
            if j+1 < COLS and i-1 >= 0 and (i-1,j+1) not in flashed:
                if main_vals[i-1][j+1] != 9: main_vals[i-1][j+1] += 1
                elif (i-1,j+1) not in to_flash: to_flash.append((i-1,j+1))
            #LEFT-DOWN
            if i+1 < ROWS and j-1 >= 0 and (i+1,j-1) not in flashed:
                if main_vals[i+1][j-1] != 9: main_vals[i+1][j-1] += 1
                elif (i+1,j-1) not in to_flash: to_flash.append((i+1,j-1))
            #RIGHT-DOWN
            if j+1 < COLS and i+1 < ROWS and (i+1,j+1) not in flashed:
                if main_vals[i+1][j+1] != 9: main_vals[i+1][j+1] += 1
                elif (i+1,j+1) not in to_flash: to_flash.append((i+1,j+1))
            #print(flashed)
        display_vals()
        steps += 1
        output = len(flashed)

    print("OUTPUT : " + str(steps))

def solution_prob_02():
    output = 0
    print("OUTPUT : " + str(output))


solution_prob_01()
#solution_prob_02()
