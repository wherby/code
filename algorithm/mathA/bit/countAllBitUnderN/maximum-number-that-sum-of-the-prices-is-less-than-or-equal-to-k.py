# https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/2603673/er-fen-da-an-shu-wei-dpwei-yun-suan-pyth-tkir/?envType=daily-question&envId=2024-08-21
from functools import cache
from bisect import bisect_right,insort_left,bisect_left

class Solution1:
    def findMaximumNumber(self, k: int, x: int) -> int:
        l,r =1, 10**15
        

        @cache 
        def dfs(i:int, limit_hight,acc,str):
            m= len(str)
            if i == len(str):
                return acc 
            lo =0
            hi = int(str[i]) if limit_hight else 1
            res =0 
            for d in range(lo,hi+1):
                res += dfs(i+1,limit_hight and d ==hi,acc + d *((m-i)%x ==0),str) 
            return res 
        def verify(num):
            bn = bin(num)[2:]
            return dfs(0,True,0,bn)
        while l < r:
            mid = (l+r+1)>>1
            #print(mid,verify(mid))
            if verify(mid)>k:
                r = mid -1
            else:
                l = mid 
        return l


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count(num: int) -> int:
            res = 0
            i = x - 1
            n = num >> i
            while n:
                res += (n // 2) << i  ##高位
                if n % 2:
                    mask = (1 << i) - 1
                    res += (num & mask) + 1 ## 低位累计
                i += x
                n >>= x
            return res
        return bisect_left(range((k + 1) << x), k + 1, key=count) - 1

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/2603673/er-fen-da-an-shu-wei-dpwei-yun-suan-pyth-tkir/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    

#试填法
class Solution3:
    def findMaximumNumber(self, k: int, x: int) -> int:
        num = pre1 = 0
        for i in range(((k + 1) << x).bit_length() - 1, -1, -1):
            cnt = (pre1 << i) + (i // x << i >> 1)
            if cnt <= k:
                k -= cnt
                num |= 1 << i
                pre1 += (i + 1) % x == 0
        return num - 1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/2603673/er-fen-da-an-shu-wei-dpwei-yun-suan-pyth-tkir/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



N= 19999
re = Solution1().findMaximumNumber(N,1)
print(re)
re2 = Solution().findMaximumNumber(N,1)
print(re)