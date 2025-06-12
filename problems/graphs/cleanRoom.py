# https://leetcode.com/problems/robot-room-cleaner/
# 489. Robot Room Cleaner


# You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

# The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

# You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

# When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

# Design an algorithm to clean the entire room using the following APIs:

# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();

#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();

#   // Clean the current cell.
#   void clean();
# }
# Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

 

# Custom testing:

# The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.


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
        
        