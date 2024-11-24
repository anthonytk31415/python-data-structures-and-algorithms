from collections import defaultdict

# https://leetcode.com/problems/frog-jump/submissions/1460560886/
# 403. Frog Jump

# Do a Bottom's Up DP. For each ith stone, store the steps that are possible to get there
# Then iterate from i = 0 to n -1. For each i, consider the prior step for all steps. See
# what next steps you can take. If at any time you can get to the end, return True. 
# at the end of the iteration, return False, since you couldn't find any way to get to the end.


# Time: O(N^2) for each of n stones, traverse through possible n prior steps to get to next step
# Space: O(N^2) for size of adj list (what we call "prevSteps[i]")

# create stones value to index lookup for O(1) lookups
def buildStepLookup(stones): 
    stepToIndex = {}
    for i, stone in enumerate(stones):
        stepToIndex[stone] = i
    return stepToIndex


class Solution:
    def canCross(self, stones: list[int]) -> bool:
        stepToIndex = buildStepLookup(stones)        
        # prevSteps[i] = prevSteps that can get you to ith stone
        prevSteps = [set() for _ in range(len(stones))]
        prevSteps[0].add(0)
        for i in range(len(stones)): 
            for prevStep in [x for x in prevSteps[i]]: 
                for delta in [-1, 0, 1]: 
                    nextStep = prevStep + delta
                    nextStone = stones[i] + nextStep
                    if nextStone == stones[-1]: return True
                    if nextStone != stones[i] and nextStone in stepToIndex: 
                        prevSteps[stepToIndex[nextStone]].add(nextStep)
        return False
                        
s = Solution()
stones = [0,1,3,5,6,8,12,17]
# stones = [0,1,2,3,4,5,6,12]
# stones = [0,2]
print(s.canCross(stones))

