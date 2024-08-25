from heapq import heappush, heappop, heapify 
from collections import deque 

# as you traverse 

def shineLights(lights): 
    lights.sort(key = lambda x: (x[0], x[1]))
    lights = deque(lights)
    tracker = []
    endpoints = []
    count = 0
    while lights: 
        start, end = lights.popleft()
        count += 1
        tracker.append([start, count])
        heappush(endpoints, end)
        while endpoints and (not lights or endpoints[-1] < lights[0][0]): 
            curEnd = heappop(endpoints)
            count -= 1
            tracker.append([curEnd, count]) 

    while endpoints: 
        curEnd = heappop(endpoints)
        count -= 1
        tracker.append([curEnd, count]) 

    res = 0
    for i in range(len(tracker)): 
        if tracker[i][1] == 1:
            res += tracker[i+1][0] - tracker[i][0]
    return res
arr = [[-5, 2], [2, 4], [-2, 7]]
# arr = [[-5, 2], [2, 4]]



# 2 


# heapify(x)
# while x: 
#     y = heappop(x)
#     print(y)


print(shineLights(arr))