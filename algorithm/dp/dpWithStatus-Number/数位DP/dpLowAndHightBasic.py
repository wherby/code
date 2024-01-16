

from functools import cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int) -> int:
        high = str(finish)
        n = len(high)
        low = str(start)
        low = "0" *( n - len(low)) + low
        
        @cache
        def dfs(i:int, limit_low:bool, limit_hight:bool):
            if i == n:
                return 1 
            lo =int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_hight else 9
            
            res =0 
            for d in range(lo,hi+1):
                res += dfs(i+1,limit_low and d == lo, limit_hight and d ==hi)
            return res 
        
        return dfs(0,True,True)
    
print(Solution().numberOfPowerfulInt(111,123445))