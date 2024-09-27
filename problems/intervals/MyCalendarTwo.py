class MyCalendarTwo:

    def __init__(self):
        self.entries = []
        self.overlaps = []

    def pairOverlap(self, u, v): 
        return u[0] < v[1] and v[0] < u[1]

    def isOverlap(self, start: int, end: int):
        pair1 = [start, end]
        for pair0 in self.overlaps: 
            if self.pairOverlap(pair0, pair1): return True
        return False

    def processNewEntry(self, start, end): 
        pair0 = [start, end]
        for pair1 in self.entries: 
            if self.pairOverlap(pair0, pair1): 
                overlap = [max(pair0[0], pair1[0]), min(pair0[1], pair1[1])]
                self.overlaps.append(overlap)
        self.entries.append(pair0)
        return 
    
    def book(self, start: int, end: int) -> bool:
        if not self.entries: 
            self.entries.append([start, end])
            return True
        
        # if start, end overlaps anything in overlaps, then return False
        if self.isOverlap(start, end): return False
        
        # insert any overlaps, then insert into entries, 
        self.processNewEntry(start, end)
        return True

