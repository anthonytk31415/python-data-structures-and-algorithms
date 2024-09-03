

def countRangeSum(nums: list[int], lower: int, upper: int) -> int:
    count = 0
    n = len(nums)
    tree = [0]*(2*n)

    ## construct the segment tree
    for i in range(n): 
        k = n + i
        val = nums[i]
        tree[k] = val


    print(tree)
    for i in range(n-1, 0, -1): 
        tree[i] = tree[2*i] + tree[2*i + 1]
    print(tree)

    return 

nums = [1,2,3,4,5,6,7,8]
lower = 2 
upper = 4

countRangeSum(nums, lower, upper)