
from math import ceil, log2;
 

def getMid(s, e) :
    return s + (e -s) // 2
 
# Tobe redefine
def getSumUtil(st, ss, se, qs, qe, si) :
 
    if (qs <= ss and qe >= se) :
        return st[si]
 
    if (se < qs or ss > qe) :
        return 0
 
    mid = getMid(ss, se)
     
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) +getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2)
 

#Update
def updateValueUtil(st, ss, se, i, diff, si) :
    if (i < ss or i > se) :
        return
    st[si] = st[si] + diff
     
    if (se != ss) :
     
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i,diff, 2 * si + 1)
        updateValueUtil(st, mid + 1, se, i,diff, 2 * si + 2)
 
# The function to update a value in input array
# and segment tree. It uses updateValueUtil()
# to update the value in segment tree
def updateValue(arr, st, n, i, new_val) :
 
    # Check for erroneous input index
    if (i < 0 or i > n - 1) :
        print("Invalid Input", end = "")
        return
 
    # Get the difference between
    # new value and old value
    diff = new_val - arr[i]
 
    # Update the value in array
    arr[i] = new_val
 
    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0)
 
# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(st, n, qs, qe) :
 
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe) :
 
        print("Invalid Input", end = "")
        return -1
     
    return getSumUtil(st, 0, n - 1, qs, qe, 0)
 
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :
 
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se) :
     
        st[si] = arr[ss]
        return arr[ss]
     
    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se)
     
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) +constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    
    return st[si]
 
#""" Function to construct segment tree
#from given array. This function allocates memory
#for segment tree and calls constructSTUtil() to
#fill the allocated memory """
def constructST(arr, n) :
 
    # Allocate memory for the segment tree
 
    # Height of segment tree
    x = (int)(ceil(log2(n)))
 
    # Maximum size of segment tree
    max_size = 2 * (int)(2**x) - 1
     
    # Allocate memory
    st = [0] * max_size

    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0)
 
    # Return the constructed segment tree
    return st
 
# Driver Code
if __name__ == "__main__" :
 
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
 
    # Build segment tree from given array
    st = constructST(arr, n)
 
    # Print sum of values in array from index 1 to 3
    print("Sum of values in given range = ",
                       getSum(st, n, 1, 3))
 
    # Update: set arr[1] = 10 and update
    # corresponding segment tree nodes
    updateValue(arr, st, n, 1, 10)
 
    # Find sum after the value is updated
    print("Updated sum of values in given range = ",
                     getSum(st, n, 1, 3), end = "")
     
# This code is contributed by AnkitRai01