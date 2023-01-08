from functools import cache
import math
def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ps =allState(2,n)
        dic ={}
        for p in ps:
            can = []
            for i in range(n):
                if (1<<i) &p !=0:
                    can.append(nums[i])
            dic[p]= math.gcd(can[0],can[1])
        #print(dic)
        @cache
        def dfs(msk,i):
            if msk ==0 :
                return 0
            mx =1  
            for b in ps:
                if b &msk== b :
                    #print(dic[b],i)
                    mx = max(mx, dic[b] *i +dfs(msk -b,i+1) )
            return mx
        return dfs((1<<n)-1,1)

re = Solution().maxScore([3,4,6,8])
print(re)