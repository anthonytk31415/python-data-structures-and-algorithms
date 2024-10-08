# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 2952. Minimum Number of Coins to be Added

# Time: O(nlogn) for sorting
# Space: O(1) 

# Greedy Method. Invariant: at ith coin, we have maxRange where we can make all sums up from 1 to maxRange. 
# When we instantiate, we set maxRange = 0, sort coins, and start at i = 0, where i iterates across coins.
# Iterate j from 1 to target. Since we have ranges, every time we get to a coin equal to j, we can add it to our max range. 
# If j is out of the max range, increment the count, and add j to the maxRange.  

class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        i = 0
        maxRange = 0        
        res = 0
        for j in range(1, target + 1):
            while i < len(coins) and j == coins[i]: 
                maxRange += coins[i]
                i += 1
            if j <= maxRange:
                continue
            else: 
                res += 1
                maxRange += j
        return res


class Solution1:
    def minimumAddedCoins1(self, coins: list[int], target: int) -> int:
        
        def addCoinToSet(num, nums): 
            newNums = set()
            for x in nums: 
                newNums.add(x + num)
            newNums.add(num)
            nums |= newNums

        coins.sort()
        nums = set()
        nums.add(0)
        for num in coins: 
            addCoinToSet(num, nums)
        res = 0
        for i in range(1, target + 1): 
            if i in nums: continue
            res += 1            
            addCoinToSet(i, nums)
        return res


s = Solution()
coins = [1,4,10]
target = 19

coins = [1,4,10,5,7,19]
target = 19

coins = [1,1,1]
target = 20


coins =[932,312,248,200,381,978,623,803,403,861,331,923,76,876,258,122,589,992,530,151,863,380,394,613,400,929,559,162,603,569,967,45,579,350,701,847,869,740,868,95,34,185,135,308,87,192,689,756,365,93,942,190,718,246,848,539,392,346,97,743,242,607,481,362,413,583,429,851,864,812,891,656,489,465,986,530,645,928,404,912,699,942,723,381,688,75,947,715,398,908,157,517,467,26,741,82,858,219,903,268,562,253,809,466,388,152,154,909,299,180,191,331,68,575,894,854,463,524,518,381,323,566,115,943,665,638,286,141,947,820,735,714,604,793,142,447,684,315,880,54,33,22,390,79,901,799,964,386,568,849,384,189,726,923,841,625,580,379,211,611,167,200,654,148,261,783,527,646,95,103,374,178,349,935,194,583,600,75,774,667,355,132,375,228,852,746,592,196,404,679,829,141,395,133,420,751,676,600,891,285,618,284,416,758,356,753,687,320,518,168,218,789,456,682,294,570,45,133,459,642,53,706,550,885,332,118,543,465,389,274,475,191,991,779,702,96,120,558,332,271,299,817,931,66,275,645,16,611,453,329,153,376,264,150,446,653,494,801,233,495,29,668,705,678,160,386,367,213,377,440,859,433,534,89,530,987,131,772,673,64,110,323,479,738,52,39,183,421,884,465,363,683,10,726,266,244,18,379,20,473,809,413,419,340,694,296,451,554,686,323,98,774,412,826,709,128,625,100,875,48,954,887,379,145,429,713,228,314,149,651,936,789,741,36,780,707,207,98,332,421,150,884,459,520,77,541,815,314,246,264,836,350,315,774,644,477,497,967,493,347,960,726,393,791,737,72,330,88,795,695,390,358,685,43,669,783,722,895,547,535,204,435,585,401,857,805,234,493,951,313,811,603,988,676,189,724,539,878,526,454,528,289,133,972,240,175,211,122,503,245,718,786,434,411,782,834,152,464,462,52,884,728,700,145,524,814,847,646,326,797,543,409,847,333,326,580,98,176,7,138,825,860,199,254,351,106,246,407,554,348,591,212,147,535,606,664,829,767,642,859,274,433,667,510,304,397,729,500,727,633,109,574,441,577,874,177,233,228,899,281,611,600,52,357,649,464,575,888,374,367,913,370,612,162,768,312,945,785,547,430,194,723,6,592,233,455,573,4,682,703,17,93,490,651,756,546,407,839,92,466,517,173,997,244,368,836,529,910,850,24,653,549,156,860,49,6,739,31,964,246,305,827,21,711,124,558,317,554,250,441,883,934,890,619,860,432,158,712,172,374,49,144,405,272,819,915,289,83,952,358,96,759,932,844,341,57,22,895,646,781,975,713,960,279,307,188,121,735,244,630,676,798,594,726,268,281,921,683,683,387,845,501,740,862,640,448,825,757,245,532,633,313,335,498,745,800,940,825,831,721,754,370,729,327,13,895,398,464,153,852,370,592,464,191,483,924,845,311,998,201,852,678,795,25,99,664,662,745,706,379,384,257,258,616,85,670,30,165,982,114,769,975,214,629,237,252,538,51,59,922,802,1000,920,141,818,642,136,682,215,254,834,608,665,11,215,693,286,182,680,854,615,116,989,665,146,324,933,721,502]
target = 1036
print(s.minimumAddedCoins(coins, target))
        