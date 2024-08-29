from heapq import heappush, heappop

def nthUglyNumber(self, n: int) -> int:

    nums = [2,3,5]
    heap = []
    heappush(heap, [1, [0,0,0]])
    
    # calculate the next smallest 
    for _ in range(n):
        cur = heappop(heap)
        num, curCounts = cur
        for i, delta in enumerate([1, 0, 0], [0, 1, 0], [0, 0, 1]):
            newNum = 1
            newCounts = []
            for j in range(3): 
                newCount = delta[j] + curCounts[j]
                newCounts.append(newCount)
                newNum *= nums[j]*newCount
            heappush([newNum, newCounts])
    return num
