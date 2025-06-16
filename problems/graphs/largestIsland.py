# https://leetcode.com/problems/making-a-large-island/


def find_islands(grid): 
   island_members = {}
   island_edges = {}        #key = num island; [edges] = keys of other islands within 1 cell   
   
   # find islands and their contents
   # the length = area 
   
   
   # find edge to other islands: 
   # 
   
   return island_edges, island_members

    

def find_max(island_edges, island_members): 
    
    max_num = 1
    for island in island_edges: 
        for neighbor in island_edges[island]:
            cur_max = 1 + len(island_members[island]) + len(island_members[neighbor])
            max_num = max(max_num, cur_max)
    
    return max_num


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        
        island_edges, island_members = find_islands(grid)
        return find_max(island_edges, island_members) 