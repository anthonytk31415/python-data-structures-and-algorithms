
# all evaluations will be effective 

# onlyy call when stack hits "("
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
            # print(stack)
            if x == ",": continue
            if x == ")":      
                curRes = evaluate(stack)
                if stack: 
                    stack.append(curRes)
                else: 
                    return convertStringToBool(curRes)
            else: 
                stack.append(x)
                
s = Solution()

# expression = "&(|(f))"
expression = "|(f,f,f,t)"

print(s.parseBoolExpr(expression))