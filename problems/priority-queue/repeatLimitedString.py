from heapq import heapify, heappush, heappop
from collections import Counter

# https://leetcode.com/problems/construct-string-with-repeat-limit/
# 2182. Construct String With Repeat Limit

# Time: O(nlogn) for maintaining the priority queue
# Space: O(n) for the priority queue

def improvesRes(res, char): 
    return res + char > res

def buildCharQueueValue(char, freq): 
    if freq == 0: return [] 
    return [-ord(char), char, freq]

def growRes(res, curChar, curFreq, repeatLimit):
    numLeftover = max(0, curFreq - repeatLimit)
    charGrow = min(curFreq, repeatLimit)
    return res + curChar*charGrow, buildCharQueueValue(curChar, numLeftover)  

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:        
        repeat, res = None, ""            
        queue = [buildCharQueueValue(char, charCount) for char, charCount in Counter(s).items()]
        heapify(queue)
        while queue:          
            curCharVal, curChar, curFreq = heappop(queue)            
            if not improvesRes(res, curChar): break
            leftovers = []
            # if the repeat queue is empty or curOrd is largest, add max amt 
            addVal = 1
            if repeat == None or curCharVal < repeat[0]: addVal = repeatLimit
            res, leftovers = growRes(res, curChar, curFreq, addVal)          
            if repeat != None: 
                heappush(queue, repeat)
                repeat = None
            # if there are "leftovers", bind to repeat to reset later            
            if leftovers: 
                repeat = leftovers
        return res