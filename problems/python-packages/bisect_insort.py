from bisect import insort


nums = [1,4,2,8,7,0,9]
nums.sort()

insort(nums, 3)
print(nums)


nums = [(1, 'a'),(4, 'd'),(2, 'z'),(8, 'n'),(7, 'e'),(0, 'f'),(9, 'p')]
nums.sort(key = lambda x: x[1])

insort(nums, (3, 'd'), key = lambda x: x[1])

print(nums)