from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache




def bs(ls,t):
    n = len(ls)
    l,r = 0, n-1
    
    while l < r:
        mid = (l+r)>>1
        if ls[mid] ==t:
            return True
        elif ls[mid]< t:
            l = mid +1
        else:
            r = mid-1
    return ls[l] == t

def query(ls,t):
    if ls[0] <= ls[-1]:
        return  bs(ls,t)
    else:
        return find1(ls,t)

def find1(ls,t):
    
    if len(ls) == 1:
        if ls[0] != t:
            return False
        return True
    n = len(ls)
    mid = n //2 
    lst,rst = ls[:mid],ls[mid:]
    return query(lst,t) or query(rst,t)

def find(ls,t):
    while ls[-1] == ls[0] and len(ls) >1:
        ls.pop()
    return  find1(ls,t)

#
ls = [ 6,7,8,9,11,12, 12,12,12,12,12]


# L,  R
# [6,6,6,6,1,2,3,5] 
#
# target =15
# print(find(ls,10))

for i in range(20):
    print((find(ls,i)) , i in ls,i)


# 证明pop最右值之后操作的正确性
# 一个扭曲的排序数组，可以分为左有序和右有序数列,  [A...C...][...D...B]              
# 因为在最开始的时候做了pop操作消除重复值，所以左有序数列最左（最小值)A 一定大于右有序的最右(最大值)B，  A>B
# 同理，如果是二分之后的子数组还是扭曲的排序数组，则子数组一定由左有序和右有序的子数组构成， 其中左数列的子数组的最左端点C 和右有序数列的最右D,在有序数列里 一定存在 C>=A >B >=D  【因为构成子数组的左右部分一定是左有序和右有序数列的子序列，左有序的子序列的左端点一定相对于原数组靠右，大于等于最小值A，右有序的子序列右端点一定小于最大值B】

# 从上可知，预处理pop之后如果首尾相等的子序列一定不是扭曲数列。
    
# 如果把 if ls[0] <= ls[-1] 改为 if ls[0] < ls[-1] 则在数组中间的重复元素会使得算法退化为O(n)