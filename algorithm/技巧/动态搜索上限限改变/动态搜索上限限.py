# https://leetcode.cn/contest/weekly-contest-525/problems/count-frequency-staircase-subarrays-ii/description/
# 动态变化的搜索上下限
# 如果直接搜索的话会OT
# /Users/tao/software/code/contest/00000c490d177/c525/q4

from collections import defaultdict,deque

from sortedcontainers import SortedDict,SortedList

from collections import Counter, defaultdict, deque




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

    firstLs = SortedList([])
    for val, indices in lls.items():
      firstLs.add((indices[0], val))

    for i in range(n):
      cmax = n
      cmin = i
      for k1 in range(len(firstLs)):
        if k1 >= len(vls) or cmin > cmax:
          break

        pos, val = firstLs[k1]

        if len(lls[val]) < k1 + 1:
          break

        cmin = max(cmin, lls[val][k1])
        if len(lls[val]) > k1 + 1:
          cmax = min(cmax, lls[val][k1 + 1])

        if cmin < cmax and cmin <= i + vls[k1] - 1 < cmax:
          ans += 1  

      val_i = nums[i]
      if lls[val_i] and lls[val_i][0] == i:
        firstLs.remove((i, val_i))
        lls[val_i].popleft()
        if lls[val_i]:
          firstLs.add((lls[val_i][0], val_i))

    return ans




re =Solution().countStaircase([5,8,8,2,2,2])
print(re)