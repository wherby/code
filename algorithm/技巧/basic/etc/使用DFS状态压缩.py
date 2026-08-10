# 使用DFS的时候，设计状态是更容易碰撞的，这样可以很好压缩数据规模，在选择对的时候，利用对称性也可以压缩数据规模
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        n = len(demand)

        @cache
        def dfs(i, r0, r1, w0, w1):
            if i == n:
                return (0, 0)

            d = demand[i]
            best_count = 0
            best_wait = float('inf')

            is_symmetric = (r0 == r1 and w0 == w1)

            if r0 >= d:
                wait_i = w0                         
                next_w0 = d                           
                next_w1 = max(0, w1 - wait_i)          
                
                sub_count, sub_wait = dfs(i + 1, r0 - d, r1, next_w0, next_w1)
                count = 1 + sub_count
                max_wait = max(wait_i, sub_wait)

                if count > best_count:
                    best_count = count
                    best_wait = max_wait
                elif count == best_count:
                    best_wait = min(best_wait, max_wait)

            if r1 >= d and not is_symmetric:
                wait_i = w1                            
                next_w0 = max(0, w0 - wait_i)         
                next_w1 = d                            

                sub_count, sub_wait = dfs(i + 1, r0, r1 - d, next_w0, next_w1)
                count = 1 + sub_count
                max_wait = max(wait_i, sub_wait)

                if count > best_count:
                    best_count = count
                    best_wait = max_wait
                elif count == best_count:
                    best_wait = min(best_wait, max_wait)

            if best_count == 0:
                return (0, 0)

            return (best_count, best_wait)

        total_served, min_wait = dfs(0, fuel[0], fuel[1], 0, 0)
        dfs.cache_clear()
        return min_wait if total_served > 0 else -1