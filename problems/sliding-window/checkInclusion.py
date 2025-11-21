from collections import Counter

#sliding window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        s1Counter = Counter([x for x in s1])
        s2Counter = Counter(s2[:(n-1)])
        for right in range(n-1, m): 
            # add right window
            s2Counter[s2[right]] +=1
            if s1Counter == s2Counter: 
                return True
                       
            # take off ending char
            left = right-n+1
            s2Counter[s2[left]] -=1
            if s2Counter[s2[left]] == 0: 
                del s2Counter[s2[left]]

        return False       