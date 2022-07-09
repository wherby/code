# https://leetcode.cn/contest/zj-future2022/problems/NBCXIp/
# https://leetcode.cn/contest/zj-future2022/ranking/1/
from collections import Counter 
from functools import lru_cache
class Solution:
    def minTransfers(self, distributions) -> int:
        cnt = Counter()
        for i,j,num in distributions:
            cnt[i] -= num
            cnt[j] += num
        res = 0
        values = [i for i in cnt.values() if i!=0]
        m = len(values)
        
        @lru_cache(None)
        def dfs(state,cur):
            if state == (1<<m) - 1:
                return 0
            res = float('inf')
            for i in range(m):
                if state & (1<<i) == 0:
                    res = min(res, (cur+values[i]!=0) + dfs(state|(1<<i),cur+values[i]))
            return res
        
        return dfs(0,0)