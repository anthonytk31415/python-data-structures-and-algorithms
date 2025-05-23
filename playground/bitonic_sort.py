

# n = 2**m for m in {0, 1, 2, ...}
# 

def do_layer(layer, direction, i):
    for j from i-1 down to 0: 
        for each element b in the block: 
            if that element has not been compared with in this loop: 
                compare b to (b + 2**j) and swap according to direction 
                (e.g. "low to high" direction places low in lower index, 
                high in higher index and vice versa)  

def bitonic_sort(array):
    for i from 1 to m: 
        split the array of size n/2**i into equal, 
            disjoint partitions of size 2**i, called layers
        direction = low to high 
        for each layer: 
            do_layer(layer, direction, i)
            direction = swap direction from 
                high to low <--> low to high and vice versa 
