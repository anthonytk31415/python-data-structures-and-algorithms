from typing import List
from heapq import heappush_max, heappop_max, heapify_max
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)           # user_id = set(friends)
        self.newsfeed = defaultdict(list)           # list = [time, userid, tweetid]
        self.tweets = defaultdict(list)             # list = [time, userid, tweetid]; append only;
        self.K = 10
        self.time = 0

    # (1) save tweet to your tweet record; (2) fanout to followers
    def postTweet(self, userId: int, tweetId: int) -> None:
        curTime = self.time 
        self.time += 1        
        self.tweets[userId].append([curTime, userId, tweetId])
        tweetObj = [curTime, userId, tweetId]
        
        heappush_max(self.newsfeed[userId], tweetObj)      
        
        # fanout 
        for followee in self.followees[userId]:             
            heappush_max(self.newsfeed[followee], tweetObj)           

    # O(KlogK) to pop the first 10 items
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        temp= [] 
        for _ in range(self.K): 
            if not self.newsfeed[userId]: 
                break
            popped = heappop_max(self.newsfeed[userId]) 
            temp.append(popped)
            res.append(popped[2])       
        while temp: 
            heappush_max(self.newsfeed[userId], temp.pop())
        return res
        
    # remove tweets in newsfeed from unfollowerId
    def purgeTweets(self, followerId, unfollowerId): 
        new_list = [x for x in self.newsfeed[followerId] if x[1] != unfollowerId]
        heapify_max(new_list)
        self.newsfeed[followerId] = new_list

    # 
    def publishTweets(self, followerId, followeeId): 
        tweets = self.tweets[followeeId]
        for tweet in tweets: 
            heappush_max(self.newsfeed[followerId], tweet)
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followerId not in self.followees[followeeId]: 
            self.followees[followeeId].add(followerId)
            self.publishTweets(followerId, followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 
        if followerId in self.followees[followeeId]: 
            self.followees[followeeId].remove(followerId)        
            self.purgeTweets(followerId, followeeId)