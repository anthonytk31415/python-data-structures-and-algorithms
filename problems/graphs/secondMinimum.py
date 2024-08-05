# https://leetcode.com/problems/second-minimum-time-to-reach-destination/?envType=daily-question&envId=2024-07-28
# 2045. Second Minimum Time to Reach Destination

from collections import defaultdict, deque

# Use bfs to traverse with a special twist: 
# you can visit each node no more than twice. anything after that, it becomes redundant. 
# Return the time you hit the destination (n) for a second time. 
# apply some rules for the wait-at-light logic 

# Time: O(V+E) - traverse each vertex and edge at most twice, and then do that Lights calc
# across nodes visited, at most O(V). 
# Space: O(V+E)

def secondMinimum(n: int, edges: list[list[int]], time: int, change: int) -> int:
    graph = defaultdict(list)
    for u, v in edges: 
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start): 
        visited = {x: 0 for x in range(1, n+1)}
        res = []
        q = deque()        
        q.append([0 , start])
        while q: 
            curCount, u = q.popleft()
            if visited[u] <= 0: 
                visited[u] += 1
                if u == n: 
                    res.append(curCount)
                    if len(res) == 2:
                        break 
                for v in graph[u]: 
                    if visited[v] <= 0: q.append([curCount + 1, v])        
        return res
    
    def lights(totalNodes): 
        curTime = 0
        greenTime = 0 + change      ## time when next light turns red
        nodes = 0
        while nodes < totalNodes: 
            if curTime < greenTime: 
                nodes += 1
                curTime += time 
            else: 
                greenTime += change
                curTime = greenTime 
                greenTime += change
        return curTime

    numNodes = bfs(1)
    print("numnodes: ", numNodes)
    res = lights(numNodes[1])
    return res

n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5

n = 2
edges = [[1,2]]
time = 3
change = 2

n = 19
edges = [[1,2],[2,3],[1,4],[2,5],[2,6],[2,7],[7,8],[8,9],[7,10],[9,11],[11,12],[1,13],[3,14],[13,15],[14,16],[8,17],[4,18],[11,19],[17,11],[3,19],[19,7],[12,5],[8,1],[15,7],[19,6],[18,9],[6,8],[14,19],[13,18],[15,2],[13,12],[1,5],[16,18],[3,16],[6,1],[18,14],[12,1],[16,6],[13,11],[1,14],[16,13],[11,16],[4,15],[17,5],[5,9],[12,2],[4,10],[9,16],[17,9],[3,5],[10,2],[18,1],[15,18],[12,17],[10,6],[10,18],[19,12],[12,15],[19,13],[1,19],[9,14],[4,3],[17,13],[9,3],[17,10],[19,10],[5,4],[5,7],[14,17],[1,10],[4,11],[6,4],[5,10],[7,14],[8,14],[18,17],[15,10],[11,8],[14,11],[7,3],[5,18],[13,8],[4,12],[11,3],[5,15],[15,9],[8,10],[13,3],[17,1],[10,11],[15,11],[19,2],[1,3],[7,4],[18,11],[2,14],[9,1],[17,15],[7,13],[12,16],[12,8],[6,12],[9,6],[2,17],[15,6],[16,2],[12,7],[7,9],[8,4]]
time = 850
change = 411

print(secondMinimum(n, edges, time, change))