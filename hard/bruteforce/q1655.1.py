from functools import lru_cache 
from collections import Counter 
class Solution(object):
    def canDistribute(self, nums, quantity):
        m = len(quantity)
        quantity.sort()

        @lru_cache
        def dp(con,i):
            if i ==-1:
                return True
            
            if quantity[i] > con[0]:
                return False
            
            for j in range(len(con)):
                if con[j] >= quantity[i]:
                    new_con = list(con)
                    new_con[j] -= quantity[i]
                    new_con.sort(reverse=True)

                    if dp(tuple(new_con),i-1):
                        return True
                else:
                    break
            return False
        return dp(tuple(t for _, t in Counter(nums).most_common(m)),m-1)

nums=[420,420,420,235,687,420,420,591,759,420,420,420,326,756,420,376,420,989,387,212,420,89,420,420,326,420,420,420,387,387]
q=[1,3,1,4]
re =Solution().canDistribute([1,2,3,3] , [2])
print(re)

