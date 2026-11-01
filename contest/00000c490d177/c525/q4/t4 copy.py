from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from collections import Counter
from bisect import bisect_left
from collections import Counter, defaultdict, deque


from collections import Counter, defaultdict, deque
from sortedcontainers import SortedList


class Solution:

  def countStaircase(self, nums: list[int]) -> int:
    n = len(nums)
    ans = 0

    lls = defaultdict(deque)
    for i, a in enumerate(nums):
      lls[a].append(i)

    vls = []
    t_idx = 1
    while True:
      t = (t_idx + 1) * t_idx // 2
      if t > n:
        break
      vls.append(t)
      t_idx += 1

    for k1_idx, length in enumerate(vls):
      k1 = k1_idx + 1
      if length > n:
        break

      curr_lls = {k: deque(v) for k, v in lls.items()}


      c = Counter()
      for i in range(length):
        c[nums[i]] += 1

      firstLs = SortedList()
      for val in c:
        firstLs.add((curr_lls[val][0], val))

      for i in range(n - length + 1):
        if len(c) == k1:
          isGood = True
          for j, (pos, val) in enumerate(firstLs):
            if c[val] != j + 1:
              isGood = False
              break
          if isGood:
            ans += 1

        if i + length < n:
          left_val = nums[i]
          right_val = nums[i + length]
          is_new_right = right_val not in c or c[right_val] == 0

          c[left_val] -= 1
          if c[left_val] == 0:
            del c[left_val]
          c[right_val] += 1

          firstLs.remove((i, left_val))
          curr_lls[left_val].popleft()
          if curr_lls[left_val] and curr_lls[left_val][0] <= i + length:
            firstLs.add((curr_lls[left_val][0], left_val))

          if is_new_right:
            firstLs.add((i + length, right_val))

    return ans






re =Solution().countStaircase([5,8,8,2,2,2])
print(re)