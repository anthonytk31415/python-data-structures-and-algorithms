# https://leetcode.com/problems/largest-rectangle-in-histogram/


# Monotonic Stack: 
# Keep a monotonic stack of heights: iterate across each h in heights.
# When we pop larger heights from the stack, we process its height and width 
# using the ith endpoint. Since all popped are larger than its predecessor, 
# we can use i to define the total rectangle. 
# 
# Then when we are ready to append the new height index, since we popped larger 
# ones, we actually retain the width of the last popped w/ the current height to 
# be popped by mutating heights[last_popped], since when it's ready to be popped
# and thus processed, the width should be counted from that popped time. 

# We append 0 at the end of heights to process the entire stack at the end. 

# O(n) Time and Space Complexity: Iterating once across the heights and 
# for the stack. 
 
def largestRectangleArea(heights): 
    heights.append(0)
    maxRect = 0
    stack = []
    for i in range(len(heights)): 
        cur = None
        while stack and heights[stack[-1]] >= heights[i]: 
            cur = stack.pop()
            maxRect = max(heights[cur]*(i - cur), maxRect)
        if cur is not None:  
            stack.append(cur)
            heights[cur] = heights[i]
        else: 
            stack.append(i)
    return maxRect



def largestRectangleArea1(heights): 

    heights.append(0) # append 0 allows you to give the min height the max width of the entire heights array. Same wiht the -1 in stack.
    incStack = [-1]

    maxRect = 0
    for i, curHeight in enumerate(heights):
        while incStack and curHeight < heights[incStack[-1]]:
            height = heights[incStack.pop()]
            width = i - incStack[-1] - 1
            maxRect = max(maxRect, height*width)
        incStack.append(i)
    heights.pop()
    return maxRect


heights = [2,1,5,6,2,3]
# heights = [2,4]
print(largestRectangleArea(heights))