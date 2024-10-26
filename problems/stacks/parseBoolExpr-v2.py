# https://leetcode.com/problems/parsing-a-boolean-expression/description/
# 1106. Parsing A Boolean Expression

# Traverse the array. Throw all elements into a stack but ignore ",", 
# until you hit ')'. Then Evaluate the expression with all of the 
# arguments by popping the stack and converting. Note that the first ")"
# you encounter will evaluate the innermost evaluation. Then after that one, 
# each argument will be evaluated, and you can safely evaluate the 
# expression. 

# Time: O(n) for traversing once and then evaluating the expression once
# Space: O(n) for the stacks
 

# only call when stack hits "("
def getOperator(stack):
    stack.pop()
    return stack.pop()

def convertBoolToString(bool): 
    if bool: return "t"
    return "f"

def convertStringToBool(string): 
    return string == "t"

def applyOperator(operator, expr): 
    print(operator, expr)
    res = expr[0]
    if operator == "!": 
        return convertBoolToString(not res)
    if operator == "|": 
        for i in range(1, len(expr)):
            res |= expr[i]
    elif operator == "&": 
        for i in range(1, len(expr)):
            res &= expr[i]
    return convertBoolToString(res)
        
def evaluate(stack):
    expr = []
    operator = ""
    while stack and stack[-1] != "(":  
        cur = stack.pop()
        expr.append(convertStringToBool(cur))
    operator = getOperator(stack)
    return applyOperator(operator, expr) 

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for x in expression: 
            if x == ",": continue
            if x == ")":      
                curRes = evaluate(stack)
                if stack: 
                    stack.append(curRes)
                else: 
                    return convertStringToBool(curRes)
            else: 
                stack.append(x)