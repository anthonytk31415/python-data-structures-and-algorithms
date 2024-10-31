# https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
# 871. Minimum Number of Refueling Stops

from collections import defaultdict
from math import inf 

# dp = you made it to i with this much fuel after collecting, doing this many stops
def dfs(i, stations, memo):
    statPos, statFuel = stations[i]
    for k in range(0, i): 
        for prevFuel in memo[k]: 
            prevStops = memo[k][prevFuel] 
            prevPos = stations[k][0]
            fuelConsumed = (statPos - prevPos)
            # you can make it: 
            if fuelConsumed <= prevFuel: 
                curFuel = prevFuel - fuelConsumed + statFuel
                # add it to memo
                stop = 1
                if i == len(stations) - 1: stop = 0
                if memo[i][curFuel]: 
                    memo[i][curFuel] = min(memo[i][curFuel], prevStops + stop)
                else: 
                    memo[i][curFuel] = prevStops + stop
    return  


# stations[i] = [pos_i, fuel_i]
class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        memo = defaultdict(lambda: defaultdict(int)) # (i) = [(fuel, stops) ]        (i, fuel) stops
        memo[0][startFuel] = 0
        stations.append([target, 0])        # ending station
        stations.append([0, startFuel])        # ending station
        stations.sort(key = lambda x: x[0])
        for i in range(1, len(stations)):
            dfs(i, stations, memo)
        if not memo[len(stations) - 1]: return -1
        res = inf
        lastStop = len(stations) - 1
        for fuel in memo[lastStop]: 
            # print("stops: ", stops)
            res = min(res, memo[lastStop][fuel])
        return res

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, s: list[list[int]]) -> int:
        dp = [startFuel] + [0]* len(stations)
        for i in range(len(s)): 
            for t in range(i + 1, -1, -1): 
                if dp[t] >= s[i][0]: 
                    dp[t + 1] =  max(dp[t+1], dp[t] + s[i][1])
        for t, d in enumerate(dp): 
            if d >= target: return t
        
        return -1



s = Solution()
target = 1
startFuel = 1
stations = []

print(s.minRefuelStops(target, startFuel, stations))