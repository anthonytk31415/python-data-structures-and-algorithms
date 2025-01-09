# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/


# DP with left and right: calculate the running some of ones on left and the number of moves 
# required to move everything on the left to the current i. 
# Do the same with the right. 
# At the end, take the total moves for each i. 
# time and space: O(n); can probably optimize but this looks good

def convert_to_array(boxes): 
    res = []
    for x in boxes: 
        if x == "0": res.append(0)
        else: res.append(1)
    return res

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        boxes = convert_to_array(boxes)
        sum_r, sum_l, moves_l, moves_r, total_moves= [0]*len(boxes), [0]*len(boxes), [0]*len(boxes), [0]*len(boxes), [0]*len(boxes)
        for i in range(1, len(sum_l)): 
            sum_l[i] = boxes[i] + sum_l[i-1]
            moves_l[i] = moves_l[i-1] + sum_l[i]
        
        for i in range(len(sum_r)-2, -1, -1): 
            sum_r[i] = boxes[i] + sum_r[i+1]
            moves_r[i] = moves_r[i+1] + sum_r[i]
          
        # build total
        for i in range(len(total_moves)): 
            total_moves[i] = moves_r[i] + moves_l[i]
        return total_moves