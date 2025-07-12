# https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solutions/825860/dpmei-ju-xia-yi-lun-liang-ming-xuan-shou-okfu/?envType=daily-question&envId=2025-07-12
# 如果直接坐标系处理，很难处理 na,nb的循环，其实循环处理的应该是两者间的距离
# 这样写下去错误
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dfs(m,a,b):
            if a == m-b:
                return (1,1)
            mx,mn = 1,10
            nm = (m+1)//2 
            print(m,nm,a,b)
            na=nb = -1
            for i in range(1,nm+1):
                if i == a  or m+1 - i ==a :
                    na = i
                if i == b or m+1 -i == b:
                    nb = i 
            print(na,nb)
            if na > nb:
                na,nb = na,nb
            for i in range(1,na+1):
                for j in range(2,nb+1):
                    tmx,tmn = dfs(nm,i,j)
                    mx = max(mx,tmx+1)
                    mn = min(mn,tmn+1)
            return (mx,mn)
        mx,mn = dfs(n,firstPlayer,secondPlayer)
        return [mn,mx]

re = Solution().earliestAndLatest(n = 5, firstPlayer = 1, secondPlayer = 5)
print(re)