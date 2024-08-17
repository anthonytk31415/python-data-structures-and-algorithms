from collections import Counter
from bisect import bisect_right

# https://leetcode.com/problems/online-election/solutions/3526018/python3-solution-beats-91-11-quibler7/
# 911. Online Election

class VoteDay: 
    def __init__(self, t, winner=None, winnerNumVotes=0, counter=Counter()):
        self.t = t
        self.winner = winner
        self.winnerNumVotes = winnerNumVotes
        self.counter = counter

    def copy(self):
        return VoteDay(self.t, self.winner, self.winnerNumVotes, self.counter.copy())
    
    def addVote(self, candidate):
        self.counter[candidate] += 1
        if self.counter[candidate] >= self.winnerNumVotes: 
            self.winnerNumVotes = self.counter[candidate]
            self.winner = candidate


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        self.votes = []         # votes[i] = VoteDay
        for i in range(len(persons)):
            self.addVote(i, persons, times)

    def q(self, t: int) -> int:
        idx = bisect_right(self.votes, t, key = lambda x: x.t)
        return self.votes[idx - 1].winner

    def addVote(self, i, persons, times):
        candidate, t = persons[i], times[i]
        newVoteDay = None       
        if not self.votes: 
            newVoteDay = VoteDay(t)
        else: 
            newVoteDay = self.votes[-1].copy()
            newVoteDay.t = t
        newVoteDay.addVote(candidate)
        self.votes.append(newVoteDay)

# x = Counter("anthony")  



persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]
v = TopVotedCandidate(persons, times)

for x in [3, 12, 25, 15, 24, 8]:
    print(v.q(x))