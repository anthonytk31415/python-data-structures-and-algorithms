# https://leetcode.com/problems/beautiful-array/description/
# 932. Beautiful Array


from collections import deque



def beautifulArray(n: int) -> list[int]:
    arr = [1,3,2] 
    while len(arr) < n:    
        even = [2*x for x in arr]
        odd =  [x - 1 for x in even]
        arr = odd + even

    if len(arr) > n: 
        end = len(arr)
        for x in range(n + 1, end + 1):
            arr.remove(x)
    return arr







# garbage below
def beautifulArray3(n: int) -> list[int]:
    res = deque([])
    def isBeautiful(res): 
        m = len(res)
        for i in range(m-1): 
            for k in range(i+1, m - 1):
                if 2*res[k] == res[i] + res[m - 1]: return False         
        return True

    def dfs(i): 
        print(res)
        # check if currentl beautiful, if so then proceed, if not, then return False
        if not isBeautiful(res) or not isBeautiful(deque(list(res)[::-1])): return False, res
        if (n % 2 == 0 and i > n // 2) or (n % 2 == 1 and i > (n // 2 + 1)): 
            print("a beautiful res: ", res)
            return True, res
        # if i <= n // 2: proceed; attach, then dfs, then unattach

        toAppend = [i, n- i + 1]
        if i == n - i + 1: toAppend[1] = None

        res.append(toAppend[0])
        if toAppend[1] != None: 
            res.appendleft(toAppend[1])
        isFinalBeautiful, finalResult = dfs(i + 1)
        if isFinalBeautiful: return True, finalResult
        res.pop()
        if toAppend[1] != None: res.popleft()
        # reverse, then do again 
        if toAppend[1] != None: 
            res.append(toAppend[1])
        res.appendleft(toAppend[0])
        isFinalBeautiful, finalResult = dfs(i + 1)
        if isFinalBeautiful: return True, finalResult
        if toAppend[1] != None: 
            res.pop()
        res.popleft()
        return False, res


    isFinalBeautiful, finalResult = dfs(1)
    return list(finalResult)

print(beautifulArray(4))
print(beautifulArray(5))
print(beautifulArray(2))


