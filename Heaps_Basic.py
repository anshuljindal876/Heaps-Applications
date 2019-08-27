## Program implements the basic heap operations: insert, extract min and extract max
## NOTE : Defined heap SHOULD NOT support both Extract min and Extract max at once!!

import math as M

# Function swaps values at given indices in the given array and returns the changed array
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

## Function inserts a given key into the heap's key list and returns the new heap
def insert(n, h, val):
    if(n == 0):
        return [val]
    h = h + [val]
    i = n
    while(True):
        if(i%2 == 0):
            p = int(i/2) - 1
        else:
            p = M.floor(i/2)
            
        if(h[i] > h[p] or p < 0): ## Added p<0 test in case the new value is less than the primary root
            return h
        h = swap(h, i, p)
        i = p

## Function removes and returns the key with min. value. Also returns the changed heap
def extractMin(n, h):
    if(n == 0):
        return None, h
    
    val = h[0]
    h[0] = h[n - 1]
    h.pop(n - 1)
    i = 0

    while(True):
        try:
            c1_i = int(2*i) + 1
            c1 = h[c1_i]
            try:
                c2_i = int(2*i) + 2
                c2 = h[c2_i]
                
                if(h[i] < min(c1, c2)):
                    return val, h

                if(c1 < c2):
                    h = swap(h, i, c1_i)
                    i = c1_i
                else:
                    h = swap(h, i, c2_i)
                    i = c2_i
            except:
                if(h[i] < c1):
                    return val, h
                h = swap(h, i, c1_i)
        except:
            return val, h

## Function removes and returns the key with max. value. Also returns the changed heap
def extractMax(n, h):
    if(n == 0):
        return None, h
    
    val = h[h.index(max(h))]
    h[h.index(max(h))], h[len(h) - 1] = h[len(h) - 1], h[h.index(max(h))]
    h.pop(len(h) - 1)
    return val, h
        
if __name__ == '__main__':
    h = [4, 4, 8, 9, 4, 14, 9, 11, 13]
##    h = insert(len(h), h, 7)
##    h = insert(len(h), h, 10)
##    h = insert(len(h), h, 5)
##    print(h)

##    val, h = extractMin(len(h), h)
##    print(val, h)
    
    val, h = extractMax(len(h), h)
    print(val, h)
