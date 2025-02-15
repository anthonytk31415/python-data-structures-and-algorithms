# https://leetcode.com/problems/product-of-the-last-k-numbers/submissions/1542611333/
# 1352. Product of the Last K Numbers

# trick is how you handle zeros
# prefix sum
# Time per op, O(1)
# Space: O(n)
# be really careful with indices

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [0]
        self.lastZero = 0

    def add(self, num: int) -> None:
        if num == 0: toAppend = 0 
        elif self.lastZero == len(self.prefix) - 1:
            toAppend = num
        else: toAppend = self.prefix[-1]*num        
        self.prefix.append(toAppend)  
        if num == 0: self.lastZero = len(self.prefix) - 1        
              
    def getProduct(self, k: int) -> int:
        end = len(self.prefix) - 1
        if end - k + 1 <= self.lastZero: return 0
        if end - k + 1 == self.lastZero + 1: return self.prefix[-1]
        return self.prefix[-1] / self.prefix[-1-k]
            