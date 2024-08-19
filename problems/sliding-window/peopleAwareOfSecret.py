from collections import deque 

# 2327. Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/

# O(n) for n days Both Time and Space

# keep a 2 queues: 1 for delayed, 1 for active. 
# evict from actives those who will forget. 
# at each day: add delayed to active, if active, by popping from front. 
# for sum of actives, add them to delayed. 
# answer = sum of actives + sum of delayed after nth day

def peopleAwareOfSecret(n, delay, forget):
    q = deque()
    q.append([1 + delay, 1])    # q[i] = when people go to window, numPeople
    w = deque()                 # w[i] = when they forget, numPeople 
    wSum, qSum = 0, 1
    for day in range(1, n+1):
        # remove people from window who forget
        if w and w[0][0] <= day: ## double check bounds
            wSum -= w[0][1]
            w.popleft()

        # add people from queue to window
        if q and q[0][0] == day: 
            w.append([q[0][0] + forget - delay, q[0][1]])
            wSum += q[0][1]
            qSum -= q[0][1]
            q.popleft()

        # add num window to queue: live people tell someone 
        if wSum > 0: 
            q.append([day + delay, wSum])
            qSum += wSum

    return wSum + qSum 

n = 6
delay = 2 
forget = 4


# n = 4
# delay = 1
# forget = 3
print(peopleAwareOfSecret(n, delay, forget))