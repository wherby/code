
from sortedcontainers import SortedList
class Solution(object):
    def minimumDeviation(self, nums):
        n = len(nums)
        sl = SortedList()
        for n in nums:
            if n %2==1:
                sl.add(n*2)
            else:
                sl.add(n)
        mx = sl[-1] -sl[0]
        while True:
            t = sl.pop(-1)
            if t %2 ==1:
                return mx
            sl.add(t//2)
            mx = min(mx, sl[-1]-sl[0])

re =Solution().minimumDeviation(nums = [1,2,3,4])
print(re)

