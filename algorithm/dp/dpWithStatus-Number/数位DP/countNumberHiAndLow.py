# https://leetcode.cn/problems/count-the-number-of-powerful-integers/description/

from functools import cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = str(finish)
        n = len(high)
        low = str(start)
        low = "0" *( n - len(low)) + low
        diff = n  -len(s)
        
        @cache
        def dfs(i:int, limit_low:bool, limit_hight:bool):
            if i == n:
                return 1 
            # lo 和hi 不能收到其他约束
            # 其他约束在for 里约束
            lo =int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_hight else 9
            
            res =0 
            if i < diff:
                for d in range(lo,min(limit,hi)+1):
                    res += dfs(i+1,limit_low and d == lo, limit_hight and d ==hi)
            else:
                x= int(s[i-diff])
                if lo<=x <= min(hi,limit):
                    res += dfs(i+1,limit_low and x == lo, limit_hight and x ==hi)
            return res 
        
        return dfs(0,True,True)