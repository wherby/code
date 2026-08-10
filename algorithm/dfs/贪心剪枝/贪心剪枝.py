# 这里有两个贪心思路
# 首先确定最多有多少位数字，利用质数个数和当前位数相比，比两者的最大值多一位一定能满足条件，
# 因为位数一定能满足条件，所以需要找到最少的位数，这里就需要先贪心填0，如果成功则不用继续求更大位数
# 而在填每位数字的时候，优先选能填的最小的数字进行DFS，如果成功则直接退回
# 这里不成功的原因是质数因子没有消耗，这里DFS的时候其实是进行试填，最多会进行 O(9**len(cnt)) 个试填, 而 cache 会对这些试填压缩，变成 O(9*len(cnt)) 次运算
# algorithm/dfs/贪心剪枝/贪心剪枝.py

from functools import cache
import math
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        cur = int(t)
        cnt = 0 
        for p in 2,3,5,7:
            while cur % p ==0:
                cnt +=1
                cur = cur //p 
        if cur >1:
            return -1 

        cnt = max( cnt - len(num) ,0)+1
        pat = "0"*cnt  + num
        
        n = len(pat)
        
        ans = ["0"]*n 
        
        acc =0
        
        @cache 
        def dfs(i,t,is_limit):
            nonlocal acc 
            acc +=1 
            if i == n:
                return t ==1 
            if is_limit and i <cnt and dfs(i+1,t,True):
                return True
            
            low = int(pat[i]) if is_limit else 0 
            for d in range(max(low,1),10):
                if dfs(i+1, t //math.gcd(t,d), is_limit and d ==low):
                    ans[i] = str(d)
                    return True
            return False
        dfs(0,t,True)
        dfs.cache_clear()
        print(acc)
        return "".join(ans).lstrip("0")

# re = Solution().smallestNumber(num = "1234", t = 256)
# print(re) 
print(7**16)
re = Solution().smallestNumber(num = "0", t = 7**15)
print(re) 