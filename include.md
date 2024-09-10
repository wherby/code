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

from math import gcd

from heapq import heapify,heappop,heappush 

from math import inf

## accumulation
from itertools import accumulate
list(accumulate((x!=y for x,y in zip(s,t)),initial =0))

##  @functools.lru_cache(None) 

from math import comb // use to combination

from sortedcontainers import SortedDict,SortedList
self.ls =SortedList()


from itertools import pairwise


## #BS
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

### 二分开区间写法 https://live.bilibili.com/1315966?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.live_users_card.0.click&live_from=86001
https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges/solutions/2908931/er-fen-da-an-zui-da-hua-zui-xiao-zhi-pyt-twe2/

left = 0, right = max(value) +1 ; check(left) == True, check(right) == False
while left +1 < right:
    mid=(left +right) >>1
    if check(mid):
        left = mid
    else:
        right = mid 
return left


### use lib
``` python
# https://leetcode.cn/problems/maximum-number-of-alloys/submissions/
# https://leetcode.cn/circle/discuss/SwCGEn/

from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        mx = 0 
        def getCost(mid,com):
            acc = 0
            for c1,s,c in zip(com,stock,cost):
                acc += max(0,c1*mid -s ) *c
            return acc
        for com in composition:
            k = bisect_right(range(10**9),budget,key=lambda x: getCost(x,com)) # line 14
            mx =max(mx,k-1)
        return mx
    
# Line 14 is bisect_right, which means need find a number which cost is more than buget,
# if ues bisect_left(range(10**9),budget,key=lambda x: getCost(x,com)) if budget could create 2.1 item, then the k will be 3, it budget could afford 3 item, then the k is 3 also 
# which is not the answer we want, if use bisect_right, then the budget could create 2.1, then k is 3, if the budget could create 3, then k is 4 , then we could use -1 to get the real k value
#  the meaning of the create 2.1:
#  getCost(2,com) < budget < getCost(3,com) which means the buget could more than afford 2 item but less than 3.
#  
``` 

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


# time function 

import time

start = time.time()
re =Solution().sumCounts( test)
print(re)
end = time.time()
print(end - start)


## Cache clear

@cache
def dfs(zeroleft,oneleft,state):
    ...
    return res%mod
ans =  dfs(zero,one,0)%mod
dfs.cache_clear()

如果不清楚cache， 会超出内存错误 https://leetcode.cn/problems/student-attendance-record-ii/submissions/
