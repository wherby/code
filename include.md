from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache

from math import gcd

from heapq import heapify,heappop,heappush 

##  @functools.lru_cache(None) 

from math import comb // use to combination

from sortedcontainers import SortedDict,SortedList
self.ls =SortedList()


from itertools import pairwise


## 
#TDK binary search 二分 格式
r = mid,l =mid +1 , mid =(l+r)>>1
r = mid,l =mid -1 , mid=(l +r +1)>>1
https://leetcode-cn.com/problems/find-in-mountain-array/submissions/
如果要写成
r=mid-1 l=mid 的情况也要转变为 r=mid, l= mid +1  最后return l-1
写成 while l<r 的循环的时候，r的值最好是一个不能取的值:  #https://leetcode-cn.com/problems/maximum-number-of-removable-characters/

https://leetcode-cn.com/problems/longest-duplicate-substring/solution/gong-shui-san-xie-zi-fu-chuan-ha-xi-ying-hae9/
l = mid, r=mid -1  , mid = (l+r+1) >>1  while l <r  

mid = (l+r)>>1 不会取到r  
mid =(l+r+1)>>1 不会取到l  如果取到这个值说明是无解情况

### use lib
 bisect_left(range(1, 1000), z, key=lambda y: customfunction.f(x, y))
 https://docs.python.org/3/library/bisect.html
 bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire list is used. If x is already present in a, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.

The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo : i]) for the left side and all(val >= x for val in a[i : hi]) for the right side.

key specifies a key function of one argument that is used to extract a comparison key from each element in the array. To support searching complex records, the key function is not applied to the x value.

If key is None, the elements are compared directly with no intervening function call.

Changed in version 3.10: Added the key parameter.

### https://leetcode.cn/contest/biweekly-contest-100/problems/minimum-time-to-repair-cars/
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        s = lambda x: sum(int(math.sqrt((x//r))) for r in ranks)
        return bisect_left(range(min(ranks) * cars * cars),cars,key=s)


### 返回时候需要对l的值进行判断
https://leetcode.cn/contest/weekly-contest-325/problems/take-k-of-each-character-from-left-and-right/
contest/00000c315d89/c325/q2/t2.py  
        return l if verify(l) else -1
#

from math import inf

# deque  https://www.geeksforgeeks.org/stack-in-python/   广度优先如果要效率可以使用
from collections import deque
 
stack = deque()

# format 
return [f"{j}/{i}" for i in range(2, n + 1) for j in range(1, i) if gcd(i, j) == 1]