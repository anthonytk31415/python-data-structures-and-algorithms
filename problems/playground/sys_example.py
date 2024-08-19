import sys
from itertools import product
print("Enter text (Ctrl+D or Ctrl+Z to stop):")

# Read K and M
K, M = map(int, input().split())
print(K, M)
# Read the K lists
lists = []
for _ in range(K):
    x = input()
    print(x)
    data = list(map(int, x.split()))[1:]  # Skip the first element (size of the list)
    lists.append(data)
    
