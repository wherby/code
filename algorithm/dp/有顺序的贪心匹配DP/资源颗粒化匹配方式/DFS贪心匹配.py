# https://leetcode.cn/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14
# 贪心排列，左边的robot一定匹配靠左的工厂
# 所以可以顺序对robot执行选择，工厂选择faidx一定只能递增，然后如果选择的数量达到limit，则选择后一个
# 
from functools import cache

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        @cache
        def dfs(idx,faidx,cnt):
            if idx == n:return 0 
            if faidx == m : return 10**20
            if cnt == factory[faidx][1]: return dfs(idx,faidx+1,0)
            if faidx == m : return 10**20
            ret = abs(robot[idx] - factory[faidx][0]) + dfs(idx+1,faidx,cnt +1)
            ret = min(ret,dfs(idx, faidx+1,0))
            return ret
        return dfs(0,0,0)