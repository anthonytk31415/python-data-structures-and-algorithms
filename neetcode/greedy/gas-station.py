# https://neetcode.io/problems/gas-station?list=neetcode150

# 

def canCompleteCircuit(gas, cost):
    if sum(cost) > sum(gas): return -1
    
    start = 0
    total = 0
    for i in range(len(gas)): 
        curTotal = gas[i] - cost[i]
        total += curTotal 
        if total < 0: 
            start = i + 1 
            total = 0
                
    return start


gas = [1,2,3,4]
cost = [2,2,4,1]

gas = [1,2,3]
cost = [2,3,2]

print(canCompleteCircuit(gas, cost))

# long stream accumulate large X--> one accumulate big Y

# X > Y