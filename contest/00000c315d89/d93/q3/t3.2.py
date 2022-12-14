# https://leetcode.cn/problems/frog-jump-ii/
class Solution(object):
    def maxJump(self, stones):
        n = len(stones)
        mx = 0
        mx = stones[1] -stones[0]
        for i in range(2,n):
            mx = max(mx,stones[i]-stones[i-2])
        return mx