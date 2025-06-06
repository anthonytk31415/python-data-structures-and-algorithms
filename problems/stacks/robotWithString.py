from collections import Counter

# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

# you want to write


# 2 operations: 
# - dequeue from s (from front), append to t (back)
# - pop t to paper
    
# s = 56
# t = 12

# --> 2156

# s 12
# t 1256

# 126521




# 125611

# s 7
# t 95



# youw ant to put the smallest elment in s first 
# if top of t is less than s, pop to res
# first, scan s for all characters. 
# go one by one, 
# at each step, make sure you pop t if t < global s min
# if cur is a global, max then bring it to res
# otherwise append

# at the end, mass pop

def get_ord(char): 
    return ord(char) - ord('a')



# def count_chars(s): 
#     counter = [0]*26
#     for x in s: 
#         idx = get_ord(x)
#         counter[idx] += 1
#     return counter

# s = "anthony"

# # returns -1 if you're at the end
# def find_global_max(idx_global_max, s): 
#     for i in range(idx_global_max, len(s)): 
#         if s[i] > 0: 
#             return i

#     return i + 1

# counter = count_chars(s)
# print(counter)
# print(find_global_max(1, counter))


# the array implementation is much faster. 

def robotWithString(s): 
    res = ""
    robot = []
    counter = Counter(s)
    min_char = min(counter.keys())
    for st in s: 
        while robot and robot[-1] <= min_char: 
            res += robot.pop()
        if st == min_char: 
            res += st
        else: 
            robot.append(st)
        counter[st] -=1
        if counter[st] == 0: del counter[st]
        if counter: min_char = min(counter.keys())                 
    while robot: 
        res += robot.pop()                
    return res


# ahn
# nt
s = "vzhofnpo"
# t = 19
# t --> 


# cc = Counter(s)

# print(min(cc.keys()))

print(robotWithString(s))
# # 12