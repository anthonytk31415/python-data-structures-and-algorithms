# https://leetcode.com/problems/smallest-common-region/description/?envType=company&envId=airbnb&favoriteSlug=airbnb-six-months
# 1257. Smallest Common Region
# Airbnb question

# DFS with an adjacency list
# O(mn) space and time for m length of regions and n max length of region

def createAdjList(regions): 
    adjList = {}
    for region in regions: 
        for i in range(1, len(region)): 
            adjList[region[i]] = region[0] 
    return adjList

def dfs_first(region, adjList, visited): 
    visited.add(region)
    if region not in adjList: return visited
    return dfs_first(adjList[region], adjList, visited)

def dfs_second(region, adjList, visited): 
    if region in visited: return region
    return dfs_second(adjList[region], adjList, visited)

class Solution:
    def findSmallestRegion(self, regions: list[list[str]], region1: str, region2: str) -> str:
        adjList = createAdjList(regions)
        visited = dfs_first(region1, adjList, set())
        return dfs_second(region2, adjList, visited)