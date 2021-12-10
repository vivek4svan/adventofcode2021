
from collections import defaultdict

with open('day_09_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    heightmap = []
    Y = len(data_lines)
    X = len(data_lines[0])
    for y in range(Y):
        heightmap.append([])
        for height in data_lines[y]:
            heightmap[y].append(int(height))

def print_heightmap():
    print(X,Y)
    for map in heightmap:
        print(map)

def solution_prob_01():
    print_heightmap()
    lowpoints = []
    coord = []
    for y in range(Y):
        for x in range(X):
            main_val = heightmap[y][x]
            if y == 0 and x == 0:
                if main_val < heightmap[y][x+1] and main_val < heightmap[y+1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y == 0 and x < X-1 and x > 0:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y][x+1] and main_val < heightmap[y+1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y == 0 and x == X-1:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y+1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y > 0 and y < Y-1 and x == 0:
                if main_val < heightmap[y-1][x] and main_val < heightmap[y+1][x] and main_val < heightmap[y][x+1]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y == Y-1 and x == 0:
                if main_val < heightmap[y-1][x] and main_val < heightmap[y][x+1]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y == Y-1 and x > 0 and x < X-1:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y-1][x] and main_val < heightmap[y][x+1]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y == Y-1 and x == X-1:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y-1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            elif y > 0 and y < Y-1 and x == X-1:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y-1][x] and main_val < heightmap[y+1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))
            else:
                if main_val < heightmap[y][x-1] and main_val < heightmap[y][x+1] and main_val < heightmap[y+1][x] and main_val < heightmap[y-1][x]:
                    lowpoints.append(main_val)
                    coord.append((y,x))

    #print("OUTPUT : " + str(lowpoints))
    print("OUTPUT : " + str(sum(lowpoints)+len(lowpoints)))
    return coord

def solution_prob_02(points):
    basin = []
    for p in points:
        print("\n___________ " + str(p) + " ___________")
        visited = []
        tovisit = [p]
        while len(tovisit) != 0:
            print(tovisit)
            print(visited)
            print("_______________________________")
            point = tovisit.pop()
            if point not in visited: visited.append(point)
            row = point[0]
            col = point[1]
            #LEFT CHECK
            if (col-1) > -1 and heightmap[row][col-1] != 9:
                if (row,col-1) not in visited: tovisit.append((row,col-1))
            #RIGHT CHECK
            if (col+1) < X  and heightmap[row][col+1] != 9:
                if (row,col+1) not in visited: tovisit.append((row,col+1))
            #UP CHECK
            if (row-1) > -1 and heightmap[row-1][col] != 9:
                if (row-1,col) not in visited: tovisit.append((row-1,col))
            #DOWN CHECK
            if (row+1) < Y  and heightmap[row+1][col] != 9:
                if (row+1,col) not in visited: tovisit.append((row+1,col))
        basin.append(len(visited))

    basin.sort()
    print("\n\nOUTPUT : " + str(basin) + " : " + str(basin[-1]*basin[-2]*basin[-3]))

solution_prob_02(solution_prob_01())
