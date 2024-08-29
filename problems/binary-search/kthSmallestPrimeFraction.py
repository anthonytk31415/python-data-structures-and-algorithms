# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# 786. K-th Smallest Prime Fraction

from heapq import heappush, heappop

def kthSmallestPrimeFraction(arr: list[int], k: int) -> list[int]:
    heap = []
    heappush(heap, [arr[0]/arr[-1], 0, len(arr) - 1])
    visited = set()
    visited.add((0, len(arr) - 1))

    for _ in range(k): 
        _, i, j = heappop(heap)
        for u, v in [(i+1, j), (i, j-1)]: 
            if u < v and (u, v) not in visited: 
                visited.add((u, v))
                heappush(heap, [arr[u]/arr[v], u, v])
    return [arr[i], arr[j]]


arr = [1,2,3,5]
k = 3

print(kthSmallestPrimeFraction(arr, k))