# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# 1190. Reverse Substrings Between Each Pair of Parentheses

# use a stack to keep track of elements. When you hit a ")", reverse the ones until you hit "(". Put it back in the stack.
# O(N^2) Time, Space; O(N)

def applyReverse(stack): 
    queue = []
    while stack[-1] != "(":
        queue.append(stack.pop())
    stack.pop() # pop the "("
    for x in queue: 
        stack.append(x)
    return 

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s: 
            if char == ")": 
                applyReverse(stack)
            else: 
                stack.append(char)

        return "".join(stack)
    
s = "(ed(et(oc))el)"
s = "(u(love)i)"
s = "(abcd)"
s = "abcd"
sol = Solution()
print(sol.reverseParentheses(s))
    

