def next_permutation(arr):
    arr = list(arr)  # Ensure it's a list if a tuple is given
    n = len(arr)
    # Step 1: Find the pivot
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1    
    if i == -1:
        return arr[::-1]  # Already the last permutation, return first permutation
    # Step 2: Find the next larger element to swap
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    # Step 3: Swap pivot and successor
    arr[i], arr[j] = arr[j], arr[i]
    # Step 4: Reverse the suffix
    arr[i + 1:] = reversed(arr[i + 1:]) 
    return arr


# arr = [1,2,3,4]
# a = arr
# for i in range(25): 
#     a = next_permutation(a)
#     print(a)
