# 1564. Put Boxes Into the Warehouse I
# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/description/

def maxBoxesInWarehouse(boxes: list[int], warehouse: list[int]) -> int:

    largest = [x for x in warehouse]
    for i in range(1, len(largest)): 
        largest[i] = min(largest[i-1], largest[i])

    print(largest)
    boxes.sort()
    j = 0
    # count = 0
    for i in range(len(largest) - 1, -1, -1): 
        if j >= len(boxes): break
        if boxes[j] <= largest[i]: 
            j += 1
    return j

boxes = [4,3,4,1]
warehouse = [5,3,3,4,1]

boxes = [1,2,2,3,4]
warehouse = [3,4,1,2]
print(maxBoxesInWarehouse(boxes, warehouse))