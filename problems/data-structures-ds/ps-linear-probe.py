# Deletion for linear probing using eager delete


# first, find key and blank cell: 
i = h(k)
while A[i] has the wrong key: 
    i = (i + 1) % N
if A[i] is empty: 
    raise exception             # the key doesn't exist
A[i] = empty                    # you found the key; now mark the i empty

# Then, pull other keys forward:

j = (i + 1) % N
while A[j] nonempty:
    k = key in A[j]             
    if h(k) <= i < j (mod N):   # is k's hash between original i and current j? 
        A[i] = A[j]             # swap
        A[j] = empty
        i = j
    j = (j + 1) % N
    
