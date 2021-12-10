
from collections import defaultdict

with open('day_08_input.txt') as f:
    data_lines = [data.strip() for data in f.readlines()]
    streams = []
    for line in data_lines:
        signal = line.split("|")[0].split()
        digits = line.split("|")[1].split()
        streams.append([signal,digits])

def solution_prob_01():
    ctr = 0
    unique_seg = []
    for S in streams:
        for s in S[1]:
            if len(s) in (2,3,4,7):
                ctr += 1
                unique_seg.append(s)
    print(unique_seg)
    print("OUTPUT : " + str(ctr))

def all_char_exists(s1,s2):
    for s in s1:
        if s not in s2:
            return False
    return True

def no_char_exists(s1,s2):
    for s in s1:
        if s in s2:
            return False
    return True

def calc_digits(S):
    digits = defaultdict(int)
    for s in S:
        if len(s) == 2:
            digits[1] = s
        elif len(s) == 3:
            digits[7] = s
        elif len(s) == 4:
            digits[4] = s
        elif len(s) == 7:
            digits[8] = s
    S.remove(digits[1])
    S.remove(digits[4])
    S.remove(digits[7])
    S.remove(digits[8])

    for s in S:
        if len(s) == 5 and all_char_exists(s,digits[8]) and all_char_exists(digits[1],s):
            digits[3] = s
            S.remove(s)
            break
    for s in S:
        if len(s) == 6 and all_char_exists(digits[3],s) and all_char_exists(digits[4],s):
            digits[9] = s
            S.remove(s)
            break
    for s in S:
        if len(s) == 5 and all_char_exists(s,digits[9]):
            digits[5] = s
            S.remove(s)
            break
    for s in S:
        if len(s) == 5:
            digits[2] = s
            S.remove(s)
            break
    for s in S:
        if len(s) == 6 and all_char_exists(digits[1],s):
            digits[0] = s
            S.remove(s)
            break
    digits[6] = S[0]
    #print(digits)
    return digits

def solution_prob_02():
    total_sum = 0
    for S in streams:
        print(S[0])
        digits = calc_digits(S[0])
        digit_value = 0
        for input_digit in S[1]:
            for d in digits:
                if all_char_exists(input_digit,digits[d]) and len(input_digit) == len(digits[d]):
                    digit_value = (digit_value * 10) + d
        print(digit_value)
        total_sum += digit_value
    print("OUTPUT : " + str(total_sum))

#solution_prob_01()
solution_prob_02()
