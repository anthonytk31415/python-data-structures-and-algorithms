from math import inf

# The problem from 260P Discussion 9, question 1. 

# arr will in the end be sorted by starting time
# Key Invariant: maxOverlap will always be an index that has a starting time < the current comparison
# We apply mergesort. 

# O(nlogn) time, o(n) space.

def findLargestOverlap(arr, p, r): 
    if r - p <= 1: return 0
    mid = (r + p) // 2
    findLargestOverlap(arr, p, mid)
    findLargestOverlap(arr, mid + 1, r)
    answer = merge(arr, p, mid, mid + 1, r)
    return answer

def merge(arr, p, q, w, r): 
    t = [None]*(r - p + 1)
    i = p
    j = w
    k = 0
    maxOverlap = 0
    maxEnd = None
    while i <= q and j <= r: 
        if arr[i].start < arr[j].start: 
            t[k] = arr[i]
            i += 1
        else: 
            t[k] = arr[j]
            j += 1
        if maxEnd == None: maxEnd = t[k].end            
        else: 
            maxOverlap = max(maxOverlap, min(maxEnd, t[k].end) - t[k].start)
            maxEnd = max(maxEnd, t[k].end)
        k += 1        
    while i <= q: 
        t[k] = arr[i]
        i += 1
        k += 1
    while j <= r: 
        t[k] = arr[j]
        j += 1
        k += 1
    # copy t to arr at the end
    for x in range(len(t)):
        arr[p + x] = t[x]
    return maxOverlap