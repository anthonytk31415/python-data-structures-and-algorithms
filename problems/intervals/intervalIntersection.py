# https://leetcode.com/problems/interval-list-intersections/description/?envType=problem-list-v2&envId=52dlem1s
# 986. Interval List Intersections


# Intervals. Use merge sort like algorithm. 

def intervalIntersection(firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
    def isOverlap(a, b): 
        return a[0] <= b[1] and b[0] <= a[1]

    def getIntersection(a, b): 
        return [max(a[0], b[0]), min(a[1], b[1])]

    i = j = 0
    res = []
    while i < len(firstlist) and j < len(secondlist): 
        a, b = firstlist[i], secondlist[j]
        if isOverlap(a, b): 
            c = getIntersection(a, b)
            res.append(c)
        if a[1] < b[1]: 
            i += 1
        else:  
            j += 1

    # while i < len(firstlist): 
    #     res.append(firstlist[i])
    #     i += 1
    # while j < len(secondlist): 
    #     res.append(secondlist[j])
    #     j += 1
    return res

# firstList = [[0,2],[5,10],[13,23],[24,25]]
# secondList = [[1,5],[8,12],[15,24],[25,26]]

firstList = [[3,5],[9,20]]
secondList = [[4,5],[7,10],[11,12],[14,15],[16,20]]

print(intervalIntersection(firstList, secondList))