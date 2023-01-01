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