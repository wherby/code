class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        sm = 0
        sl = []
        for a,b in tasks:
            sl.append((a-b,a))
        sl.sort()
        dp = 0
        sm = 0
        for b,a in sl:
            dp = max(dp, sm +a -b)
            sm +=a
        return dp

re =Solution().minimumEffort([[1,2],[2,4],[4,8]])
print(re)