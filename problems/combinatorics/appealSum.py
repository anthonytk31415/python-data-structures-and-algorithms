# https://leetcode.com/problems/total-appeal-of-a-string/description/
# 2262. Total Appeal of A String

# very similar to this: 
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/submissions/1405491041/

# Instead of counting distinct characters in a substring, try: 
# For a character, count the number of distinct substrings that contain that index of the char. 
# zyxx for y, that'll be 2*3 = 6: zy, zyx, zyxx, y, yx, yxx (num of chars on left + 1) * (num of chars on right + 1) 
# When we have multiple characters, we still want to pick up only one occurance of the substring.
# For example: zyxxy
# For the first y, we have zyxxy and everything in between, including zy, zyx, zyxx, zyxxy, y, yx, yxx, yxxy. So 2*4 = 8 = left*right
# for the second y, we have xxy, xy, y: 3*1 = 3
# So by convention we just take the chars from the left up to the last y, or all the way. 
# And for the right limit, we take it all the way. This convention avoids double counting.   

# Combinatorics problem, although it can be done with DP?

# Complexity: O(n) time, O(1) space

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