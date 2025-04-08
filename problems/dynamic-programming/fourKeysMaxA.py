# https://leetcode.com/problems/4-keys-keyboard/?envType=study-plan-v2&envId=dynamic-programming-grandmaster
# 651. 4 Keys Keyboard

def determine_0(cur, prev):
    maxEntry = prev[0]
    for i in range(1, len(prev)):         
        if prev[i][0] > maxEntry[0]: 
            maxEntry = prev[i]            
    (a, b, c) = maxEntry
    cur[0] = (a + 1, b, c)
    return 

def determine_1(cur, prev):
    maxEntry = prev[0]
    for i in range(1, len(prev)):         
        if prev[i][0] > maxEntry[0]: 
            maxEntry = prev[i]            
    (a, b, c) = maxEntry
    cur[1] = (a, a, c)    
    return 

def determine_2(cur, prev):
    maxEntry = prev[0]
    for i in range(1, len(prev)):         
        if prev[i][0] > maxEntry[0]: 
            maxEntry = prev[i]            
    (a, b, c) = maxEntry
    cur[1] = (a, a, c)    
    return 

def determine_3(cur, prev):
    return 

def determine_max(prev): 
    return max([x[0] for x in prev])

def maxA(n): 
    cur = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
    prev = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]

    for _ in range(n): 
        determine_0(cur, prev)
        determine_1(cur, prev)
        determine_2(cur, prev)
        determine_3(cur, prev)
    
        prev, cur = cur, [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    

    return determine_max(prev)