# 1072. Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/

# Each row and its "binary flip" is a state. Keep a count of all the rows and its flipped states 
# The one with the largest count is the answer. 

# Note we use a bitmask array to make it easier for lookups, just like the project in Algorithms.
# Use the left and right shifts.

# Time: O(n*m) for matrix traversal; 
# Space: O(m+n)


from collections import defaultdict

def buildBitmask(n): 
    bitmask, mask = [], 1
    for _ in range(n): 
        bitmask.append(mask)
        mask <<= 1
    return bitmask

def encodeRow(row, bitmask, truthVal): 
    encoded = 0    
    for i in range(len(row)):
        if row[i] == truthVal: 
            encoded += bitmask[i]
    return encoded

def encodeTrueAndFalseRow(row, bitmask):
    encoded =  encodeRow(row, bitmask, 1)
    return [encoded, encoded ^ (1 << len(row)) - 1]

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        rowTracker = defaultdict(int)
        bitmask = buildBitmask(len(matrix[0]))
        for row in matrix: 
            for encodedRow in encodeTrueAndFalseRow(row, bitmask):
                rowTracker[encodedRow] += 1            
        overallMax = 1
        for encodedRow in rowTracker: 
            overallMax = max(overallMax, rowTracker[encodedRow])            
        return overallMax
    
    
bitmask = buildBitmask(3)
row = [1,1,1]
# print(encodeRow(row, bitmask))