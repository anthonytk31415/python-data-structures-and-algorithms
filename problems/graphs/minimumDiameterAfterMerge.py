from typing import List 
from collections import defaultdict
from math import inf

# 3203. Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/

# A really good problem
# find centroid of the two. Connect. Find length from centroid to min node.


def build_adj_list(edges): 
    adj = defaultdict(list)
    for u, v in edges: 
        adj[u].append(v)    
        adj[v].append(u)
    return adj    

def dfs(node, dist_to_get_here, adj, visited, distance): 
    visited.add(node)
    min_dist_of_children = inf
    for child in adj[node]: 
        if child not in visited: 
            cur_dist = dfs(child, dist_to_get_here + 1, adj, visited, distance)
            min_dist_of_children = min(min_dist_of_children, cur_dist)
    
    res = min(dist_to_get_here, 1 + min_dist_of_children)
    distance[node] = res
    return res

def find_min_center(edges):
    start = edges[0][0]
    adj = build_adj_list(edges)
    visited = set()
    distance = {}
    dfs(start, 0, adj, visited, distance)
    min_dist = min(distance.values())
    return min_dist 


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        return 1 + find_min_center(edges1) + find_min_center(edges2)