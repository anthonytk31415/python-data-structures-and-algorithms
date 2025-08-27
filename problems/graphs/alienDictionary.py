from collections import defaultdict, Counter

# Time and space

def createDataStore(words, i, adj, inDegree, outDegree):
    if len(words) == 1: 
        return 

    chain = []
    commonWordsList = []
    commonWords = []
    for word in words:
        if i >= len(word): 
            continue
        if commonWords and commonWords[-1][i] != word[i]:
            chain.append(commonWords[-1][i])
            commonWordsList.append(commonWords)
            commonWords = []
        commonWords.append(word)
    chain.append(commonWords[-1][i])
    commonWordsList.append(commonWords)
    commonWords = []
    for k in range(len(chain)-1):
        u, v = chain[k], chain[k+1]
        adj[u].append(v)
        inDegree[v] += 1
        outDegree[u] += 1
    for x in commonWordsList:
        createDataStore(x, i+1, adj, inDegree, outDegree)


def dfs(x, visited, adj): 
    
    if visited[x] == 1: return False, []
    path = [x]
    visited[x] = 1
    for y in adj[x]: 
        if visited[y] != 2: 
            curRes, path= dfs(y, visited, adj)
            if curRes == False: 
                return False, []
            path +   
    
    visited[x] = 2

def main(words):
    adj = defaultdict(list)
    allChars = set()
    for word in words: 
        
        allChars |= set([x for x in word])
    
    
    inDegree = Counter()
    outDegree = Counter()
    createDataStore(words, 0, adj, inDegree, outDegree)
    inDegreeZero = [x for x in allChars if x not in inDegree]
    outDegreeZero = [x for x in allChars if x not in outDegree]
    print("indegrees", inDegreeZero, outDegreeZero)
    if len(inDegreeZero) > 1 or len(outDegreeZero) > 1: return False
    
    
    visited = {x: 0 for x in allChars}
    

    
words = ["hrn","hrf","er","enn","rfnn"]
print(main(words))