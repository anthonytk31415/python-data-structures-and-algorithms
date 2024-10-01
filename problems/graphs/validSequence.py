# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/
# 3302. Find the Lexicographically Smallest Valid Sequence

# O(mn) Time, O(mn) Space
# dfs implementation. kind of ambiguous - the problem makes you think that N^2 is too slow, but it's not. 

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        visited = set()
        sol = []

        def dfs(i, j, flag, w1, w2, visited, sol): 
            if j >= len(w2): return True
            if i >= len(w1): return False
            if (i, j, flag) in visited: return False
            found = False

            # if i, j are equal, move to the next
            if w1[i] == w2[j]: 
                found = dfs(i + 1, j + 1, flag, w1, w2, visited, sol)
                if found: 
                    sol.append(i)
                    return found
            # if i, j not equal and flag == 1: move to next with flag = 0
            else: 
                if flag:
                    found = dfs(i+1, j + 1, 0, w1, w2, visited, sol)
                    if found: 
                        sol.append(i)
                        return True
                # if i, j not equal, flag == 0: find the next i that is equal to j
                while i < len(w1) and w1[i] != w2[j]: 
                    i += 1
                if i < len(w1): 
                    found = dfs(i + 1, j + 1, flag, w1, w2, visited, sol)
                    if found: 
                        sol.append(i)
                        return True                
            visited.add((i, j, flag))
            return found
        
        if dfs(0, 0, 1, word1, word2, visited, sol) and len(word2) == len(sol):
            return sol[::-1]
        else: return []
    
s = Solution()
arr = [["vbcca", "abc"], ["baazzcbcz", "abcz"], ["bacdc", "abc"], ["baacb","abc" ], ["cacbd", "abc"], [ "aaaaaa", "aaabc"], ["cbbccc", "bb"], ["cddcdcccdcddddcdccccdd", "ccd"]]
for u, v in arr: 
    print(u, v, s.validSequence(u, v))

# for u, v in arr: 
#     print(u, v, s.validSequence(u, v))
# 0,1, 2
# 0, 6, 7,8
# # 1,2,4
# 1,2,3
# 1,3,4
# []
# 0, 1
# 0 , 1, 4