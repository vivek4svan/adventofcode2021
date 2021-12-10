
with open('day_10_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    #main_vals = [[int(val) for val in line] for line in data_lines]
    ROWS = len(data_lines)
    #COLS = len(data_lines[0])

chunk_dict = {
    "]":"[",
    "}":"{",
    ")":"(",
    ">":"<",
}
val_dict = {
    "]":57,
    "}":1197,
    ")":3,
    ">":25137,
}
def solution_prob_01():
    stack = []
    corrupt_chunk = []
    output = 0
    for data in data_lines:
        print("Processing : " + data)
        for chunk in data:
            if chunk in "([{<":
                stack.append(chunk)
            elif chunk in ")]}>":
                last_chunk = stack.pop()
                #print("Last Chunk Popped : " + last_chunk)
                if chunk_dict[chunk] != last_chunk:
                    corrupt_chunk.append(chunk)
                    break
    print(corrupt_chunk)
    for chunk in corrupt_chunk:
        output += val_dict[chunk]
    print("OUTPUT : " + str(output))

chunk_dict2 = {
    "[":"]",
    "{":"}",
    "(":")",
    "<":">",
}
chunk_score = {
    "]":2,
    "}":3,
    ")":1,
    ">":4,
}
def solution_prob_02():
    corrupt_chunk = []
    output = []
    for data in data_lines:
        stack = []
        #print("Processing : " + data)
        corrupt_flag = False
        for chunk in data:
            if chunk in "([{<":
                stack.append(chunk)
            elif chunk in ")]}>":
                last_chunk = stack.pop()
                #print("Last Chunk Popped : " + last_chunk)
                if chunk_dict[chunk] != last_chunk:
                    corrupt_chunk.append(chunk)
                    corrupt_flag = True
                    break
        if not corrupt_flag and len(stack) > 0:
            tot_score = 0
            print(stack)
            while len(stack) > 0:
                chunk = stack.pop()
                tot_score = (tot_score*5) + chunk_score[chunk_dict2[chunk]]
            output.append(tot_score)
    output.sort()
    print("OUTPUT : " + str(output[len(output)/2]))


#solution_prob_01()
solution_prob_02()
