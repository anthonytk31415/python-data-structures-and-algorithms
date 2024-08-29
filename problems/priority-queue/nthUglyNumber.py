from heapq import heappush, heappop

# here's a heap implementation. O(nlogn) time for the heap operations. O(n) space.  
def nthUglyNumber(n: int) -> int:
    primes = [2,3,5]
    heap = [1]
    tracker = set([1])
    for _ in range(n):
        curNum = heappop(heap)
        for prime in primes:
            newNum = curNum*prime 
            if newNum not in tracker: 
                tracker.add(newNum)
                heappush(heap, newNum)
    return curNum


# whats the DP solution? 
# def nthUglyNumber(n: int) -> int:
#     prev = 1
#     cur = 1
#     for _ in range(n-1):         
#         cur = min(prev*2, prev*3, prev*5)
#         prev, cur = cur, 1
#     return prev


n = 5
print(nthUglyNumber(n))



