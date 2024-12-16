# https://leetcode.com/problems/maximum-average-pass-ratio
# 1792. Maximum Average Pass Ratio

# Time O(nlogn) using a priority queue, space O(n)
# greedy. keep the priorty queue by largest potential change. step one at a time. 


from heapq import heappop, heappush

def potentialChange(numPass, numTotal): 
    return numPass/numTotal - ((numPass + 1) / (numTotal + 1))    

def calculateAverage(pq):     
    return sum([numPass/numTotal for _, numPass, numTotal in pq])/len(pq)

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:        
        pq = []
        for numPass, numTotal in classes: 
            heappush(pq, [potentialChange(numPass, numTotal), numPass, numTotal])                    

        while extraStudents > 0: 
            _, numPass, numTotal = heappop(pq) 
            heappush(pq, [potentialChange(numPass +1, numTotal + 1), numPass +1, numTotal + 1])    
            extraStudents -= 1        
        return calculateAverage(pq)