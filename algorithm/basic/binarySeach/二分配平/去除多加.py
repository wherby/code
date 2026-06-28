# https://leetcode.cn/problems/maximum-total-value/
class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        mod = 10**9+7
        
        def verify(mid):
            acc = 0 
            for a,d in zip(value,decay):
                if a >= mid:
                    acc += (a-mid)//d +1
            return acc >= m 
        l = 0
        r = max(value)
        while l < r:
            mid = (l+r+1)>>1
            if verify(mid):
                l=mid
            else:
                r = mid-1
        sm = 0
        cnt = 0 
        for a,d in zip(value,decay):
            if a >=l:
                c1 =  (a-l)//d 
                sm += (a*2 - c1*d)*(c1+1)//2 
                sm %=mod
                cnt += c1+1
                #print(cnt,c1,sm,a,d,l)
        return (sm - (cnt-m)*l)%mod
