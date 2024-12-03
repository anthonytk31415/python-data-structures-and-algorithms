class Building:
    def __init__(self, left, ht, right):
        self.left = left
        self.ht = ht
        self.right = right

class Strip:
    def __init__(self, left=0, ht=0):
        self.left = left
        self.ht = ht

class SkyLine:
    def __init__(self, cap):
        self.arr = []
        self.capacity = cap
        self.n = 0

    def count(self):
        return self.n

    def merge(self, other):
        res = SkyLine(self.n + other.n)
        h1, h2, i, j = 0, 0, 0, 0
        while i < self.n and j < other.n:
            if self.arr[i].left < other.arr[j].left:
                x1, h1 = self.arr[i].left, self.arr[i].ht
                maxh = max(h1, h2)
                res.append(Strip(x1, maxh))
                i += 1
            else:
                x2, h2 = other.arr[j].left, other.arr[j].ht
                maxh = max(h1, h2)
                res.append(Strip(x2, maxh))
                j += 1
        while i < self.n:
            res.append(self.arr[i])
            i += 1
        while j < other.n:
            res.append(other.arr[j])
            j += 1
        return res

    def append(self, st):
        if self.n > 0 and self.arr[self.n-1].ht == st.ht:
            return
        if self.n > 0 and self.arr[self.n-1].left == st.left:
            self.arr[self.n-1].ht = max(self.arr[self.n-1].ht, st.ht)
            return
        self.arr.append(st)
        self.n += 1

    def print_skyline(self):
        print("Skyline for given buildings is")
        for i in range(self.n):
            print(" ({}, {}),".format(self.arr[i].left, self.arr[i].ht), end="")
        print()

def find_skyline(arr, l, h):
    if l == h:
        res = SkyLine(2)
        res.append(Strip(arr[l].left, arr[l].ht))
        res.append(Strip(arr[l].right, 0))
        return res
    mid = (l + h) // 2
    sl = find_skyline(arr, l, mid)
    sr = find_skyline(arr, mid+1, h)
    res = sl.merge(sr)
    return res

arr = [Building(1, 11, 5), Building(2, 6, 7), Building(3, 13, 9), Building(12, 7, 16), Building(14, 3, 25), Building(19, 18, 22), Building(23, 13, 29), Building(24, 4, 28)]
n = len(arr)
skyline = find_skyline(arr, 0, n-1)
skyline.print_skyline()