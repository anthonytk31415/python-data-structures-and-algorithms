# https://leetcode.com/problems/course-schedule/description/
# 207. Course Schedule

from collections import defaultdict, deque

def canFinish1(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    visited = [0]*numCourses # 0 = not visited, 1 = visited, 2 = closed
    cycle = [False]
    for u, v in prerequisites:
        graph[u].append(v)

    def dfs(u):
        if u in graph: 
            for v in graph[u]: 
                if visited[v] == 1: 
                    cycle[0] = True
                    return
                if visited[v] == 0: 
                    visited[v] = 1
                    dfs(v)
        visited[u] = 2

    for u in range(numCourses):
        if visited[u] == 0: 
            visited[u] = 1
            dfs(u)
            if cycle[0]: return False

    return True



def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    inDegrees = {x:0 for x in range(numCourses)}
    q = deque()
    for u, v in prerequisites:
        graph[u].append(v)
        inDegrees[v] += 1
    for u in range(numCourses):
        if inDegrees[u] == 0: 
            q.append(u)
    while q: 
        u = q.popleft()
        if u in graph: 
            for v in graph[u]:
                inDegrees[v] -= 1
                if inDegrees[v] == 0: 
                    q.append(v)

    for x in inDegrees: 
        if inDegrees[x] > 0: return False

    return True



numCourses = 2
prerequisites = [[1,0]]

numCourses = 2
prerequisites = [[1,0],[0,1]]

numCourses = 3
prerequisites = [[0,2],[1,2],[2,0]]

# numCourses = 5
# prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(canFinish(numCourses, prerequisites))