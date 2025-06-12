# https://leetcode.com/problems/robot-room-cleaner/

# Do a DFS/Backtracking algorithm. Say you start at (0,0). Then create
# a visited set and figure out a scheme to "move" and keep track of 
# coordinates. 

# Time and space complexity: 
# O(mn) for mn size of the matrix you are traversing. For space and time..


DIR_ROTATION = {
    'UP': 0,
    'RIGHT': 1, 
    'DOWN': 2, 
    'LEFT': 3     
}

DIR_DELTA =  {
    'UP': [0,1],
    'RIGHT': [1,0], 
    'DOWN': [0,-1], 
    'LEFT': [-1,0]     
}

OPPOSITE_DIRECTION = {
    'UP': 'DOWN',
    'RIGHT': 'LEFT', 
    'DOWN': 'UP', 
    'LEFT': 'RIGHT'    
}


DIRECTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT']

def get_new_position(position, dir): 
    (x, y) = position
    (dx, dy) = DIR_DELTA[dir] 
    return (x + dx, y + dy)

def turn_around(robot): 
    for _ in range(2): 
        robot.turnLeft()

def rotate(robot, dir):
    num_turns = DIR_ROTATION[dir]
    for _ in range(num_turns):
        robot.turnRight()
        
def unrotate(robot, dir): 
    num_turns = DIR_ROTATION[dir]
    for _ in range(num_turns):
        robot.turnLeft()
    
def dfs(robot, visited, position): 
    robot.clean()
    visited.add(position)
    for dir in DIRECTIONS:
        new_position = get_new_position(position, dir)
        if new_position not in visited:
            rotate(robot, dir)        
            if robot.move(): 
                unrotate(robot, dir)
                dfs(robot, visited, get_new_position(position, dir))
                rotate(robot, OPPOSITE_DIRECTION[dir])
                robot.move()
                unrotate(robot, OPPOSITE_DIRECTION[dir])
        # return back to neutral position                    
            else: 
                unrotate(robot, dir)

class Solution:
    def cleanRoom(self, robot):
        visited = set()
        dfs(robot, visited, (0,0))
        
        