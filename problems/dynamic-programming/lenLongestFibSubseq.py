# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# 873. Length of Longest Fibonacci Subsequence

from collections import defaultdict

# Given a target, fib[target] has list of lengths and the prev value. 
# So if fib[target] exists, you can extend the fib, possibly to 
# multiple values if its length > 1. 
# Then at each i, you make pais with nums from 0 to i-1 to make 
# candidates for larger fib targets.  

# Time, Space: O(n^2)

def lenLongestFibSubseq(arr):
    fib = defaultdict(list)  # target: [[len, lastVal]]
    maxLength = 0
    for i, num in enumerate(arr): 
        if num in fib: 
            for pair in fib[num]: 
                oldLen, prevVal = pair            
                fib[num + prevVal].append([oldLen + 1, num])
                maxLength = max(maxLength, oldLen + 1)
        for num1 in arr[:i]:
            fib[num1 + num].append([2, num])
    return maxLength


arr = [1,2,3,4,5,6,7,8]
# arr = [1,3,7,11,12,14,18]

arr = [2,4,7,8,9,10,14,15,18,23,32,50]


print(lenLongestFibSubseq(arr))
