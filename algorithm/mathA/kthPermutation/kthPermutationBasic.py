
from math import factorial
from collections import Counter
import math

def get_kth_permutation(arr, k):
    arr.sort()  # Ensure the array is sorted for lex order
    result = []
    return helper(arr, k, result)

def helper(arr, k, result):
    if not arr:
        return result
    # Count the frequency of each element in the remaining array
    count = Counter(arr)
    for num in sorted(set(arr)):  # Iterate through unique elements in order
        if count[num] == 0:
            continue
        # Compute the number of permutations starting with 'num'
        # Total permutations = (n-1)! / (product of (count[c]! for all c in remaining counts))
        # Here, we adjust the counts by reducing the count of 'num' by 1
        temp_count = count.copy()
        temp_count[num] -= 1
        denominator = 1
        for c in temp_count:
            denominator *= factorial(temp_count[c])
        total = factorial(len(arr) - 1) // denominator
        if k > total:
            k -= total
            continue
        # Choose 'num', reduce its count, and proceed
        result.append(num)
        new_arr = arr.copy()
        new_arr.remove(num)  # Remove the first occurrence of 'num'
        return helper(new_arr, k, result)
    return result  # in case k is out of bounds


def perm(arr):
    c=Counter(arr)
    sz = len(arr)
    res = 1
    for v in c.values():
        res *= math.comb(sz,v)
        sz -= v
    return res

def fromPermutaionGetKth(arr):
    n = len(arr)
    def getIdxPerm(idx):
        if idx == n:
            return 1
        acc = 0
        arrTmp= list(arr[idx:])
        ks = set(arrTmp)
        ks=sorted(list(ks))
        for k in ks:
            if k < arr[idx]:
                arrTmp.remove(k)
                acc += perm(arrTmp)
                arrTmp.append(k)
            elif k == arr[idx]:
                return acc + getIdxPerm(idx+1)
    return getIdxPerm(0)


        


ls = [1,1,3,4,5,6]
print(get_kth_permutation(ls,33))
ls2 = get_kth_permutation(ls,34)
print(fromPermutaionGetKth(ls2))
print(perm(ls),)
print(get_kth_permutation(ls,1))

# https://codeforces.com/gym/105335/problem/I
ls2 = [7,4,6,9,5,3,8,2,1]
ls2 = [2,1,3]
allP = perm(ls2)
k1 = fromPermutaionGetKth(ls2)

k2 = (k1+allP//2)%allP 
k2 = allP if k2 ==0 else k2 # 因为 permutation是 1 index 的，所以需要对0 特殊处理
print(k1,k2,allP)
print(get_kth_permutation(ls2,k2))