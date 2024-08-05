from heapq import heappush, heappop, heapify

# heap doesnt work. Mis-interpreted the question.

# def minHeightShelves(books: list[list[int]], shelfWidth: int) -> int:
#     heap = []
#     for thick, height in books: 
#         heappush(heap, (-height, -thick))
#     residuals = []
#     curWidth, curHeight, totalHeight = 0, 0, 0
#     while heap or residuals: 
#         if -heap[0][1] + curWidth <= shelfWidth: 
#             curHeight = max(curHeight, -heap[0][0])
#             curWidth += -heap[0][1]
#             heappop(heap)
#         else: residuals.append(heappop(heap)) 
#         if curWidth == shelfWidth or not heap: 
#             while residuals: heappush(heap, residuals.pop())
#             totalHeight += curHeight
#             curWidth, curHeight = 0, 0         
#     return totalHeight



# Here, we traverse linearly for each i. This is an O(N) Time and O(1) answer. 
# We only need the prior iteration. 
# We keep track of whether we continue or start a new, for prev and cur. 
# For curNew, we take the min height from prev new and prev cont. 
# for curCont, we take prev new or min, whichever has lower height, and only 
# if the width has room. Otherwise, we start a new shelf. 

def minHeightShelves(books: list[list[int]], shelfWidth: int) -> int:
    # books = [thickness, Height]
    # prevNew = [totalThickness, curHeight, baseHeight, totalHeight]
    books = [[0,0]] + books 
    prevNew, curNew, prevCont, curCont = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] 
    for i in range(1, len(books)):
        curTh, curHt = books[i] 
        curNew = [curTh, curHt, min(prevNew[3], prevCont[3]), min(prevNew[3], prevCont[3]) + curHt]        
        # default: put new unit in new
        curCont = [x for x in curNew]

        # can't put it in prev.Cont; and fits in prevNew --> put it in prevNew        
        if curTh + prevCont[0] > shelfWidth and curTh + prevNew[0] <= shelfWidth: 
            curCont = [prevNew[0] + curTh, max(curHt, prevNew[1]), prevNew[2], prevNew[2] + max(curHt, prevNew[1])]  

        # fits in prev Cont; pick cont or new
        elif curTh + prevCont[0] <= shelfWidth: 

        # put block in prevCont; 2 conds: (1) doesnt fit in prevNew; (2) prevcont total height < prevNew total height
            if curTh + prevNew[0] > shelfWidth or (curTh + prevCont[0] <= shelfWidth and prevCont[2] 
                                                    + max(prevCont[1], curHt) < prevNew[2] + max(prevNew[1], curHt)):
                curCont = [prevNew[0] + curTh, max(prevCont[1], curHt), prevCont[2], prevCont[2] + max(prevNew[1], curHt)]

        # put block in prevNew: fits in both; but prevNew has lower height
            elif curTh + prevNew[0] <= shelfWidth and prevNew[2] + max(prevNew[1], curHt) <= prevCont[2] + max(prevCont[1], curHt):
                curCont = [prevNew[0] + curTh, max(prevNew[1], curHt), prevNew[2], prevNew[2] + max(prevNew[1], curHt)]

        # print("curTh: {}, curHt: {}, prevNew: {}, prevCont: {}, curNew{}, curCont: {}".format(curTh, curHt, prevNew, prevCont, curNew, curCont))

        prevNew, curNew = curNew, [0,0,0,0]
        prevCont, curCont = curCont, [0,0,0,0]
    return min(prevNew[3], prevCont[3])


books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4

# books = [[1,3],[2,4],[3,2]]
# shelfWidth = 6


books = [[7,3],[8,7],[2,7],[2,5]]
shelfWidth = 10

print(minHeightShelves(books, shelfWidth))

# print((0,2) < (0, 3))
# print((0, 9) < (0, 10))

## examples: 

## 


