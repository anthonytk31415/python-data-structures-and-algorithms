# https://leetcode.com/problems/count-number-of-teams/description/?envType=daily-question&envId=2024-07-29
# 1395. Count Number of Teams

## find a the longest monotonic sequence 

def numTeams(rating):
    def ascending(rating, ascending): 
        numsGreater = {} # key = i for index, value = how many numbers greater than the one at index i
        for i in range(len(rating)):
            count = 0
            for j in range(i+1, len(rating)): 
                if ascending: 
                    if rating[i] < rating[j]: count += 1
                else: 
                    if rating[i] > rating[j]: count += 1

            numsGreater[i] = count
        overallCount = 0
        for i in range(len(rating)):
            curCount = 0
            for j in range(i+1, len(rating)):
                if ascending: 
                    if rating[i] < rating[j]: curCount += numsGreater[j]
                else: 
                    if rating[i] > rating[j]: curCount += numsGreater[j]

            overallCount += curCount 

        return overallCount

    return ascending(rating, True) + ascending(rating, False)



rating = [2,5,3,4,1]

# print(ascending(rating, True), ascending(rating, False))