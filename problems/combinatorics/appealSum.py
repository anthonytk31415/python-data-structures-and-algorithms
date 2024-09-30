from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:
        index = defaultdict(list)
        for i, char in enumerate(s):
            if char not in index: 
                index[char].append(-1)
            index[char].append(i)

        for char in index: 
            index[char].append(len(s))
        
        count = 0
        for char in index: 
            curIndex = index[char]
            for j in range(1, len(curIndex) - 1): 
                start, cur, end = curIndex[j-1], curIndex[j], curIndex[len(curIndex) - 1]
                count += (cur - start) * (end - cur)
        return count

s = "abbca"
s = "code"
sol = Solution()
print(sol.appealSum(s))