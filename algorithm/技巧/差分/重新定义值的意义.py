# https://leetcode.cn/problems/jump-game-vii/?envType=daily-question&envId=2026-05-25
# 把1定义为达到的点，用差分记录区间是否有达到点


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f = [0]*n
        pre = [0]*(n+1)
        f[0] = 1
        pre[1] = 1

        for i in range(1,n):
            f[i] = i >=minJump and s[i] =="0" and pre[i-minJump+1] > pre[max(0,i-maxJump)]
            pre[i+1] = pre[i] + f[i]
        return bool(f[-1])