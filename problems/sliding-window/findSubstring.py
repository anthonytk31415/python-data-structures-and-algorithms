# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150
# 30. Substring with Concatenation of All Words

# Sliding Window
# Partition and traverse the string in blocks of len(words[0]). check 0, 3, 6, ... then 1, 4, 7, ...
# If the current word is in words, ensure the count of those total words <= waht's in words. If not, 
# remove from the left incrementally. You'll always have a valid window. Then check if you have a valid 
# complete window. Do this for starting indeces start = 0, 1 , ... len(words[0]) - 1. 

# Time: O(n^2) Space: O*(n)


from collections import Counter

def findSubstring(s, words):

    def check(curCounter, counter):
        for x in counter: 
            if counter[x] != curCounter[x]: return False
        for x in curCounter: 
            if curCounter[x] != counter[x]: return False
        return True

    wLen = len(words[0])
    res, counter = [], Counter(words)
    for i in range(0, len(words[0])):
        right = left = i
        curCounter = Counter()
        for right in range(i, len(s), wLen):
            # while you have duplicates, remove the prefix until you have no more duplicates
            curWord = s[right:(right+wLen)]
            if curWord in counter: 
                curCounter[curWord] += 1            
                while left < right and (curCounter[curWord] > counter[curWord]): 
                    curCounter[s[left:(left+wLen)]] -= 1
                    if curCounter[s[left:(left+wLen)]] == 0: del curCounter[s[left:(left+wLen)]]
                    left += wLen
                # if your thing contains all the words, return the position: right * wLen in the res
                if check(curCounter, counter):
                    res.append(left )
            else: 
                left = right + wLen 
                curCounter = Counter()
    return res

# s = "barfoothefoobarman"
# words = ["foo","bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

s = "aaaaaaaaaaaaaa"
words = ["aa","aa"]

print(findSubstring(s, words))