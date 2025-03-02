# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# 1524. Number of Sub-arrays With Odd Sum

# Dp implementation with ongoing prefix sum. Kadane inspo. 
# linear time, constant space!

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        cumeEvens, cumeOdds = 0
        priorEvens, priorOdds = 0
        curEvens, curOdds = 0
        for num in arr: 
            if num % 2 == 0: 
                curEvens = priorEvens + 1
                curOdds = priorOdds                
            else: 
                curEvens = priorOdds
                curOdds = priorEvens + 1                                

            priorEvens, priorOdds = curEvens, curOdds
            curEvens, curOdds = 0, 0
            cumeEvens += priorEvens
            cumeOdds += priorOdds
            
        return cumeOdds % (10**9 + 7)
        
        