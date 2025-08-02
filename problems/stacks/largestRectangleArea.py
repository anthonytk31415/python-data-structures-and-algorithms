# def popLarger(stack, i, maxRect, heights): 
#     cur = None
#     while stack and heights[stack[-1]] >= heights[i]: 
#         cur = stack.pop()
#         maxRect = max(heights[cur]*(i - cur), maxRect)
#     if cur is not None:  
#         stack.append(cur)
#         heights[cur] = heights[i]
#     else: 
#         stack.append(i)
#     return maxRect

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