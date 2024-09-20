# https://leetcode.com/problems/analyze-user-website-visit-pattern/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 1152. Analyze User Website Visit Pattern

from collections import defaultdict, Counter
from itertools import combinations


# Extremely tedius. be careful of the definitions: number of users who visited the path in order. 
# Combinations: order matters. 

# Time: 
# Space: 

def get3Combo(arr): 
    res = set()
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                res.add(tuple([arr[i], arr[j], arr[k]]))
    return res

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        tuples = list(zip(username, timestamp, website))
        tuples.sort(key = lambda x: x[1])   
        patterns = Counter()
        path = defaultdict(list)
        n = len(username)
        # Go through tuples to build and count patterns
        for i in range(n): 
            name, time, site = tuples[i]
            path[name].append(site)
        for name in path: 
            combos = set(list(combinations(path[name], 3)))
            # combos = get3Combo(path[name])
            for combo in combos: 
                patterns[tuple(combo)] += 1
        patterns = [(count, pat) for pat, count in patterns.items()]
        patterns.sort(key = lambda x: (-x[0], x[1]))
        return patterns[0][1]

# username = ["a","a","a","a"]
# timestamp = [1,2,3,4]
# website = ["a","b","c","d"]


# username =  ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
# timestamp = [436363475,710406388,386655081,797150921]
# website =   ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]

# username = ["h",      "eiy",        "cq",        "h",         "cq",      "txldsscx", "cq",      "txldsscx", "h",         "cq",           "cq"]
# timestamp = [527896567, 334462937,  517687281,  134127993,  859112386,   159548699,51100299,    444082139,  926837079,  317455832,    411747930]
# website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
username = ["h",      "eiy",        "cq",        "h",         "cq",      "txldsscx", "cq",      "txldsscx", "h",         "cq",           "cq"]
timestamp = [527896567, 334462937,  517687281,  134127993,  859112386,   159548699,51100299,    444082139,  926837079,  317455832,    411747930]
website = ["h","h","h","h","h","h","h","h","y","h","y"]
s = Solution()
print(s.mostVisitedPattern(username, timestamp, website))


# from itertools import combinations, permutations
# a = [1,2,3,4,5]
# print(list(combinations(a, 3)))

# a = "art"
# b = "boa"

# atuple = tuple([a])
# btuple = tuple([b])
# ctuple = atuple + btuple
# print(ctuple)
# # print(atuple)

# x = defaultdict(lambda: deque(deque))
# if "blah" not in x: 
#     for z in x["blah"]: 
#         x["blah"].append()
# for y in x: 
#     print(y)