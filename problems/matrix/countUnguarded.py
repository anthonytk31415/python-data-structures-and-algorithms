def insertObject(wall, graph, object): 
    u, v = wall
    graph[u][v] = object

def rotateGraph(graph): 
    m, n = len(graph), len(graph[0])
    rotatedGraph = [[None for _ in range(m)] for _ in range(n)]
    for i in range(m): 
        for j in range(n): 
            u = j
            v = (m -1)  - i
            rotatedGraph[u][v] = graph[i][j]
    return rotatedGraph

def applyDp(graph, state): 
    n = len(graph[0])
    for row in range(len(graph)): 
        for j in range(1, n): 
            if (graph[row][j] != -1 and graph[row][j] != -2) and (graph[row][j-1] == -2 or graph[row][j-1] == state): 
                graph[row][j] = state
                            
def countUnguarded(graph): 
    res = 0
    for u in range(len(graph)): 
        for v in range(len(graph[0])):
            if graph[u][v] == 4: res += 1
    return res

# walls = -1, guards = -2, guardDir = 0,1,2,3; 4 = unguarded
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:        
        graph = [[4 for _ in range(n)] for _ in range(m)]
        for wall in walls: 
            insertObject(wall, graph, -1)        
        for guard in guards: 
            insertObject(guard, graph, -2)        
        for state in range(4): 
            applyDp(graph, state)
            graph = rotateGraph(graph)            
        return countUnguarded(graph)                
    
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]

print("helloo world")

s = Solution()
print(s.countUnguarded(m, n, guards, walls))