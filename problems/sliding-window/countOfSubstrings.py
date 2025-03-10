
from collections import Counter

# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10
# 3306. Count of Substrings Containing Every Vowel and K Consonants II

# Use the pseudocode below on the conditions to follow the logic. 

# Basically, we use a sliding window approach with left, mid, right. 
# Btw mid and right - smallest window
# between left and right - largest window
# substrings that include right: mid - left + 1 (if smallest window is actually valid)

# in this implementation, I use ord with an array to do faster lookups than with a hash map since
# letters are a small array (relataively)

# O(n) time, O(1) space. 

def isValid(countVowels, vowels, consonants, k): 
    if consonants != k: return False
    for x in vowels:
        if countVowels[ord(x)] == 0: return False
    return True

def stillValidAfterIncMid(countVowels, word, mid, consonants, k, vowels): 
    return isValid(countVowels, vowels, consonants, k) and countVowels[ord(word[mid])] > 1

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        countVowels = [0]*(ord('z') + 1)
        left = mid = count = consonants = 0
        
        # invariant: entire window has valid k consonants;
        # between [left, mid), you can have as many vowels; from [mid, right], you have min number 
        # between mid and right, you have smallest valid, or invalid
        for letter in word: 
            # if vowel, add to set, else add to consonant
            if letter in vowels: countVowels[ord(letter)] += 1
            else: consonants += 1
            
            # if too many consonants, move left forward 
            while consonants > k:  
                if word[left] not in vowels: consonants -= 1
                left += 1
                            
            # if valid windowVowels, move right while its still valid
            while mid < left: 
                if word[mid] in vowels:  countVowels[ord(word[mid])] -= 1
                mid += 1
            
            while stillValidAfterIncMid(countVowels, word, mid, consonants, k, vowels): 
                countVowels[ord(word[mid])] -= 1
                mid += 1                    
                    
            if isValid(countVowels, vowels, consonants, k): 
                count += mid - left + 1

        return count
    
    
s = Solution()

word = "aeioqq"
k = 1
word = "aeiou"
k = 0

word = "ieaouqqieaouqq"
k = 1

word = "zammeuowyvdhwouilnjmwlqda"
k = 10

print(s.countOfSubstrings(word, k))