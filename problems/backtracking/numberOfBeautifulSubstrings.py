letter_map = {
    'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2,
    'f': 3, 'g': 3, 'h': 3, 'i': 4, 'j': 4, 'k': 4,
    'l': 5, 'm': 5, 'n': 5, 'o': 6, 'p': 6, 'q': 6,
    'r': 7, 's': 7, 't': 7, 'u': 8, 'v': 8, 'w': 8,
    'x': 9, 'y': 9, 'z': 9
}



def countExtraordinary(s): 
    count = set()
    curSum = [0]
    str = []

    def dfs(i): 
        print(i, curSum[0])
        if len(str) > 0 and curSum[0] % len(str) == 0: 
            print("candidate" , i, curSum[0], str)
            count.add("".join(str))

        if i < len(s): 
            curSum[0] += letter_map[s[i]]
            str.append(s[i])
            dfs(i+1)
            curSum[0] -= letter_map[s[i]]
            str.pop()
            if not str: 
                dfs(i+1)

    dfs(0)
    print(count)
    return len(count)

s = "bef"
print(countExtraordinary(s))