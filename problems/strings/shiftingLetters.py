# https://leetcode.com/problems/shifting-letters-ii/
# 2381. Shifting Letters II

# use a difference array to do range updates so you only have to change 2 numbers instead of n numbers
# each time you apply a shift[i]. 
# put letters as numbers and shift and modulo to get the final letter. 

# Time: O(n); Space: O(1)

# letter to i map
def build_letter_map(letters): 
    return {letter: i for i, letter in enumerate(letters)}

def build_letter_shift(s, shifts):
    letter_shift = [0]*len(s)
    for start, end, direction in shifts: 
        if direction == 0: direction = -1
        letter_shift[start] += direction 
        if end+1 < len(letter_shift): 
            letter_shift[end+1] -= direction    
    # apply letter shift cumulative
    for i in range(1, len(letter_shift)): 
        letter_shift[i] = letter_shift[i-1] + letter_shift[i]    
    return letter_shift

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        letter_shift = build_letter_shift(s, shifts)
        letters = "abcdefghijklmnopqrstuvwxyz"
        letter_map = build_letter_map(letters)
        for i in range(len(s)): 
            letter_shift[i] = (letter_shift[i] + letter_map[s[i]]) % 26
        res = ""
        for i in letter_shift: 
            res += letters[i]
        return res
    
sol = Solution()
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(sol.shiftingLetters(s, shifts))