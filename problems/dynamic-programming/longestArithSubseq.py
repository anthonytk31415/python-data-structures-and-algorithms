# delta contains the tuple as key: the delta, last, length

# 1027. Longest Arithmetic Subsequence
# https://leetcode.com/problems/longest-arithmetic-subsequence/description/

# Kind of like longest increasing subsequence but with a twist. You always keep the delta and the last index in memory. 
# O(N^2) Time and Space. 

def updateLongest(i, nums, delta): 
    curMaxLength = 1
    for k in range(i): 
        curDelta = nums[i] - nums[k] 
        curLookup = (curDelta, k)
        if curLookup in delta: 
            # print("i: {}, k: {}, ival: {}, kval: {}, delta: {}".format(i, k, nums[i], nums[k], delta[curLookup]))
            prevVal = delta[curLookup]
            delta[curDelta, i] = prevVal + 1
        else:
            delta[(curDelta, i)] = 2
        curMaxLength = max(curMaxLength, delta[(curDelta, i)])
    return curMaxLength


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        delta = {}
        maxLength = 1
        for i in range(1, len(nums)): 
            curMaxLength = updateLongest(i, nums, delta)
            maxLength = max(maxLength, curMaxLength)
        # print(delta)
        for x in delta: 
            if delta[x] == 5: print(x, delta[x], nums[x[1]])
        return maxLength 
    

nums = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
# nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
s = Solution()
print(s.longestArithSeqLength(nums))