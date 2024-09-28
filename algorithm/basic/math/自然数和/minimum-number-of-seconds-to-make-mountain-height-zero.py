from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m: int) -> bool:
            left_h = mountainHeight
            for t in workerTimes:
                left_h -= int((sqrt(m // t * 8 + 1) - 1) / 2)
                if left_h <= 0:
                    return True
            return False

        max_t = max(workerTimes)
        h = (mountainHeight - 1) // len(workerTimes) + 1
        return bisect.bisect_left(range(max_t * h * (h + 1) // 2), True, 1, key=check)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/solutions/2925848/er-fen-da-an-pythonjavacgo-by-endlessche-myg4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
# (X)*(X+1)//2 <=N find X :
#   see pic/findN.png