from collections import defaultdict, deque

# garbage
# returns smallest index possible 
def getSmallestPossible(i, res): 
    if i == 0: return 0
    return res[i-1] + 1

def change(i, val, word2, res): 
    prev = res[i]
    res[i] = val
    for j in range(i + 1, len(word2)): 
        if word2[j] == word2[i]: 
            newPrev = res[j]
            res[j] = prev
            prev = newPrev
    
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
    
        ind = defaultdict(deque)
        for i in range(len(word1)): 
            ind[ord(word1[i]) - ord('a')].append(i)

        burned = 0
        res = []
        for i in range(len(word2)): 
            wordList = ind[ord(word2[i]) - ord('a')]
            if i == 0: 
                if not wordList:
                    if burned: return []
                    burned = 1 
                    res.append(0)
                else: 
                    res.append(wordList.popleft())            
            if i > 0: 
                # condition: i is smaller than prior; so if you can, change prior; if not, change current
                if not wordList: 
                    if burned: return []
                    else: 
                        burned = 1
                        res.append(res[-1])

                elif res[-1] > wordList[-1]: 
                    if burned: return []
                    burned = 1 
                    x = getSmallestPossible(i-1, res)
                    if x == wordList[-1]: 
                        # change current
                        y = res[i-1] + 1
                        res.append(y)
                    else: 
                        res[i-1] = x
                        res.append(wordList.popleft())
                else: 
                    while wordList and wordList[0] <= res[-1]: 
                        # print(wordList)
                        wordList.popleft()
                    res.append(wordList.popleft())

        # change the first, 

        print(res)
        if not burned: 
            val = 0
            for i in range(len(res)): 
                if res[i] != val:
                    change(i, val, word2, res) 
                    break
                val = res[i] + 1
        return res




        
s = Solution()
arr = [["vbcca", "abc"], ["baazzcbcz", "abcz"], ["bacdc", "abc"], ["baacb","abc" ], ["cacbd", "abc"], [ "aaaaaa", "aaabc"], ["cbbccc", "bb"], ["cddcdcccdcddddcdccccdd", "ccd"]]
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

print(s.validSequence(arr[-1][0], arr[-1][1]))