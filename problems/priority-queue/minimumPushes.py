# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
# 3016. Minimum Number of Pushes to Type Word II

from collections import Counter
from heapq import heappush, heappop

# a priority queue problem. 
# Time: O(nlogn) for slots and the heap; 
# Space: O(n)
# notice that we use the keypad dictionary to store char to keypad. 

def minimumPushes(word: str) -> int:
    countChars = [(n, char) for char, n in Counter(word).items()]
    countChars.sort(key = lambda x: x[0])
    # put 2-9 in a heap, sorted by numchars. When inserting, put key in hash with position 
    heap = [0 for _ in range(2, 10)]
    keypad = {} # char, num pushes 
    while countChars: 
        _, curChar = countChars.pop()
        curKeypad = heappop(heap)
        keypad[curChar] = curKeypad + 1
        heappush(heap, curKeypad + 1)
    return sum([keypad[x] for x in word])