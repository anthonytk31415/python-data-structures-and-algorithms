# 1482. Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


# m bouquets with k flowers



def minDays(bloomDay: list[int], m: int, k: int) -> int:

    def checkCondition(days, m, k, bloomDay):
        countPanels, streak = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days: 
                streak += 1
                if streak == k: 
                    countPanels += 1
                    streak = 0
                    if countPanels == m: return True
            else: streak = 0            
        return False

    if m*k > len(bloomDay): return -1
    low, high = 1, max(bloomDay) # day elapsed 
    while low < high:  
        mid = (high + low) // 2
        if not checkCondition(mid, m, k, bloomDay): 
            low = mid + 1
        else: 
            high = mid
    return low 


bloomDay = [1,10,3,10,2]
m = 3
k = 1

bloomDay = [1,10,3,10,2]
m = 3
k = 2

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

print(minDays(bloomDay, m, k))
