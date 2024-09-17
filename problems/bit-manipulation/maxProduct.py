# https://leetcode.com/problems/maximum-product-of-word-lengths/?envType=problem-list-v2&envId=bit-manipulation

# 318. Maximum Product of Word Lengths

# Convert the word to a bit. then check if word1 & word2 == 0 and if so, keep track of product of lengths.
# O(n^2 + mn) time since we compare each word to another once. with space O(n) for the bit representation. 



def convertToBinary(word): 
    arr = ["0"]*26
    for w in word: 
        arr[ord(w) - ord("a")] = "1"
    return int("".join(arr), 2)

class Solution:

    def maxProduct(self, words: list[str]) -> int: 
        bins = [convertToBinary(w) for w in words]
        res = 0
        for i in range(len(words)): 
            for j in range(i + 1, len(words)): 
                if bins[i] & bins[j] == 0: 
                    res = max(res, len(words[i])*len(words[j]))
        return res
    



word = "abc"
z = convertToBinary(word)
print(z.bit_length())
print(bin(z))
# print(bin(convertToBinary(word)))

s = Solution()

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(s.maxProduct(words))