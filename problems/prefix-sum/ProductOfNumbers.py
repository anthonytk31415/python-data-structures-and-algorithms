# https://leetcode.com/problems/product-of-the-last-k-numbers/submissions/1542611333/
# 1352. Product of the Last K Numbers

# trick is how you handle zeros
# prefix sum
# Time per op, O(1)
# Space: O(n)
# be really careful with indices

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]


    def add(self, num: int) -> None:
        if num == 0: self.prefix = [1]
        else: self.prefix.append(self.prefix[-1]*num)        

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix): return 0
        return self.prefix[-1] / self.prefix[-1-k]
            