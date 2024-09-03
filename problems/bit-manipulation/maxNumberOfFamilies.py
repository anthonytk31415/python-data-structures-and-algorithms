# 1386. Cinema Seat Allocation
# https://leetcode.com/problems/cinema-seat-allocation/description/


# O(nlogn) for sorting reserved seats and O(n)to go through seats; 
# O(1) space since we process for each row
# use bitmask to check if the row is a candidate. 
# to clear a bit: use x & ~(1 << k) to clear the kth 


def maxNumberOfFamilies(n: int, reservedSeats: list[list[int]]) -> int:

    def getRowCount(num):   
        a = int("0111111110", 2)
        b = int("0111100000", 2)
        c = int("0000011110", 2)
        d = int("0001111000", 2)      
        if num & a == a: return 2
        elif num & b == b or num & c == c or num & d == d: return 1
        return 0
    
    count = 0
    reservedSeats.sort(key = lambda x: (x[0], x[1]))
    x = (1 << 10) - 1
    rowNum = x
    rowIdx = 0
    for i, j in reservedSeats: 
        if i > rowIdx:                         
            count += 2*(i - rowIdx - 1)
            if rowIdx > 0: 
                count += getRowCount(rowNum)
            rowNum = x
            rowIdx = i    
        rowNum &= ~(1<< (10 - j ))
    if rowIdx < n: 
        count += 2*(n - rowIdx)
    count += getRowCount(rowNum)
    return count 

# print(int("0111111110", 2))



n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]

# n = 4
# reservedSeats = [[4,3],[1,4],[4,6],[1,7]]

print(maxNumberOfFamilies(n, reservedSeats))


