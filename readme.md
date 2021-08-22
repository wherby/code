Java auto import SHIFT+ ALT + O

# Data structure 
https://github.com/cheran-senthil/PyRival/tree/master/pyrival/data_structures


# use structure

from collections import defaultdict
```
    dic =defaultdict(int)
```

from queue import PriorityQueue

from copy import copy, deepcopy
y = deepcopy(x)

For 2D arrays it's possible use map function:

old_array = [[2, 3], [4, 5]]
# python2.*
new_array = map(list, old_array)
# python3.*
new_array = list(map(list, old_array))

# for VS code show error about List
from typing import List

# Queue
from queue import Queue,LifoQueue,PriorityQueue

Use heapq instead of PriorityQueue to avoid OT https://docs.python.org/zh-cn/3/library/heapq.html

# bisect
https://docs.python.org/zh-cn/3.6/library/bisect.html
bisect.bisect_left(a, x, lo=0, hi=len(a))

## print queue
print(list(q.queue)) //https://stackoverflow.com/questions/54656387/printing-contents-of-a-queue-in-python


# Cache
import functools
class Solution:
    def minSpaceWastedKResizing(self, nums, k ):
        n = len(nums)
        INF =1e20
        @functools.lru_cache(None) 
        def dp(i,k):


# Py3 issue

##
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q =PriorityQueue()
        head = p = ListNode()
        for l in lists:
            if l:
                q.put((l.val,l))
TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
出现原因：

@cbmbbz In the event that two or more of the lists have the same val, this code will error out since the queue module will compare the second element in the priority queue which is a ListNode object (and this is not a comparable type).

改用py2 或者https://www.cnblogs.com/bonelee/p/12379914.html



