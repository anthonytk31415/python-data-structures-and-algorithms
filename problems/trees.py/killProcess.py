from collections import defaultdict

# DFS implementation: create adj list in dictionary form to find the key in O(1) Time
# then for the kill id, do DFS with doKill. for each child, recursively doKill. 
# For each doKill call, append id's in a list and return that list when done. 

# Time: O(n) to create the adj list, O(n) worst case to traverse the tree. 
# Space: O(n) to store each node in the adjacency list. 

def createAdjList(pid, ppid): 
    adjList = defaultdict(list)
    for pid_, parent in zip(pid,ppid): 
        if pid_ not in adjList: adjList[pid_] = []
        adjList[parent].append(pid_)
    return adjList

def doKill(kill, idsKilled, adjList): 
    idsKilled.append(kill)
    for child in adjList[kill]: 
        doKill(child, idsKilled, adjList)

class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        adjList = createAdjList(pid, ppid)                
        idsKilled = []
        doKill(kill, idsKilled, adjList)
        return idsKilled