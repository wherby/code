# https://leetcode.cn/contest/weekly-contest-509/problems/divisible-game/
# 因子数量有限(1000个数字)

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        mod = 10**9 +7 
        n = len(nums)
        fac = set()
        for a in nums:
            if a <=1: continue 
            d = 2 
            while d *d <=a:
                if a%d == 0:
                    fac.add(d)
                    fac.add(a//d)
                d +=1 
            fac.add(a)
        if len(fac) ==0:
            ret = max(nums) * -2 
            return ret %mod
        #print(fac) 
        bk  = 10**20 
        mx = -10**20 
        for k in fac:
            cur = 0 
            cmx = 0
            for a in nums:
                cur += a if a %k==0 else -a 
                cmx = max(cmx,cur)
                cur = max(0,cur)
                if cmx > mx:
                    mx = cmx 
                    bk = k 
                elif cmx ==mx and k < bk :
                    bk = k 
        return (bk*mx)%mod





re =Solution().divisibleGame( nums = [1,4,6,8])
print(re)