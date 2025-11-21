class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "": 
            return ""
    
        def isPalindrome(s, left, right): 
            if left < 0 or right >= len(s): 
                return 0
            if s[left] != s[right]: 
                return 0
            return 1 + isPalindrome(s, left - 1, right + 1)
        
        start = end = 0
        for i in range(len(s)): 
            numHops = isPalindrome(s, i-1, i+1)
            curLen = 1+2*numHops
            if curLen > len(end - start + 1): 
                start, end = i - numHops, i + numHops + 1

            numHops = isPalindrome(s, i, i+1)
            curLen = 2*numHops
            if curLen > len(end - start + 1): 
                start, end = i - numHops + 1, i + numHops         
        return s[start:end+1]