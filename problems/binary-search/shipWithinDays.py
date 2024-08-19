
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
# 1011. Capacity To Ship Packages Within D Days

# binary search the answer. 
# O(nlogn) time, space: O(1)

def shipWithinDays(weights: list[int], days: int) -> int:
    lower = max(weights)
    upper = sum(weights)
    while lower < upper: 
        curCapacity, daysNeeded, dayCapacity = (upper + lower) // 2, 1, 0
        for weight in weights: 
            if weight + dayCapacity > curCapacity: 
                daysNeeded += 1
                dayCapacity = 0
            dayCapacity += weight
        if daysNeeded > days: lower = curCapacity + 1 
        else: upper = curCapacity
    return lower


# arr = [1,2,3,4,5,6,7,8,9,10]
# # N (n+1) / 2
# print(sum(arr)) # 55

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5


weights = [3,2,2,4,1,4]
days = 3

weights = [1,2,3,1,1]
days = 4
# 10, 55, mid =32 TRUE
# 10, 31, mid =20 TRUE
# 10, 19, mid =14 FALSE
# 15, 19, mid =17 TRUE
# 15, 16, mid =15 TRUE
# 15, 14  return upper = 15 ;;; 15 answer


print(shipWithinDays(weights, days))