# https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solutions/825860/dpmei-ju-xia-yi-lun-liang-ming-xuan-shou-okfu/?envType=daily-question&envId=2025-07-12
# 如果直接坐标系处理，很难处理 na,nb的循环，其实循环处理的应该是两者间的距离
# 这样写下去错误
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dfs(n,a,b):
            #print(n,a,b)
            if a == n+1-b:
                return (1,1)
            mx,mn = 1,10
            m = (n+1)//2 
            # 把 a,b等价翻转到相对小的坐标，折叠取值空间; 并且保证 first < second
            if a +b > n+1:
                a,b = n+1-b,n+1-a 
            min_mid = 0 if b <=m else b - n//2 -1 # 如果a,b都在小半区，则可以相邻，否则中间一定隔了 b-n//2-1个其他的pair
            max_mid = b -a if b <= m else m- a # 如果a,b都在小半区，则最大相邻为b-a,否则相邻为m-a,因为a之前的pair，无论怎么选取都不会影响相邻
            for l in range(a):
                for mid in range(min_mid,max_mid):
                    tmn,tmx = dfs(m,l+1,l+mid+2)
                    mn = min(tmn,mn)
                    mx =max(tmx,mx)
            return [mn+1,mx+1]
        mn,mx = dfs(n,firstPlayer,secondPlayer)
        return [mn,mx]

re = Solution().earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4)
print(re)