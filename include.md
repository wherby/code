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
from itertools import permutations
from collections import Counter
from functools import lru_cache
from functools import cache

from math import gcd

from heapq import heapify,heappop,heappush 

from math import inf
from itertools import pairwise

## accumulation
from itertools import accumulate
list(accumulate((x!=y for x,y in zip(s,t)),initial =0))

##  @functools.lru_cache(None) 

from math import comb // use to combination

from sortedcontainers import SortedDict,SortedList
self.ls =SortedList()





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

### 浮点数二分
如果写成这样，要注意浮点数精度为10**15 15位有效数字作业， 如果l的整数部分为 10**12 则会死循环，更稳妥的方式是直接设置循环次数，或者变成整数二分 再转化为浮点数
while l + 10**(-6) <r: # 可能死循环，

#### ！！！如果2分开区间，right的值是需要不能取的值
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/?envType=daily-question&envId=2024-09-12
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l,r =0,n//2+1  ##开区间写法，r的值不能取
        
        def verify(mid):
            for i in range(mid):
                if nums[i]*2> nums[n-mid +i]:
                    return False
            return True
 
        while l +1<r:
            mid = (l+r)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid
            #print(mid,verify(mid),l,r,mid)
        return l*2


### use lib
[minimum-number-of-valid-strings-to-form-target-ii](https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/)
contest/00000c397d130/c415/q3/t3.binarySearch.py 
``` python 
        for i in range(n):
            check = lambda sz: sub_hash(i, i + sz + 1) not in sets[sz]
            sz = bisect_left(range(min(n - i, max_len)), True, key=check)
```
```python # if True in begin ,then reverse https://leetcode.cn/problems/maximum-matching-of-players-with-trainers
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l = 0
        r = min(len(players),len(trainers))

        def verify(mid):
            pl = players[:mid]
            tl = trainers[-mid:]
            return not all(p<=t for p,t in zip(pl,tl))
        return bisect_left(range(r+1),True,key =verify)-1
```


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
        
# https://leetcode.cn/problems/minimum-time-to-complete-trips/?envType=daily-question&envId=2024-10-05
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def verify(mid):
            return sum([mid//a for a in time])>=totalTrips
        return bisect_left(range(10**14),True, key= verify)
### using range(10**19) will cauese isuue "OverflowError: Python int too large to convert to C ssize_t" https://bugs.python.org/issue41860

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


## DP返回选择值

求最小选择的时候，把状态和值一起作为比较的参数，可以减少复杂度
algorithm/dp/dp保留选择排序
