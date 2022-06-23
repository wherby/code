from functools import lru_cache
class Solution:
    def sumSubarrayMins(self, A) -> int:
        MOD = 1e9 + 7
        n = len(A)
        pre = [0] * n
        nxt = [0] * n
        sp = []
        sn = []
        for i in range(n):
            while len(sp) != 0 and A[sp[-1]] >= A[i]:
                sp.pop()
            pre[i] = i + 1 if len(sp) == 0 else i - sp[-1]
            sp.append(i)
        
        for i in range(n-1, -1, -1):
            while len(sn) != 0 and A[sn[-1]] > A[i]:
                sn.pop()
            nxt[i] = n - i if len(sn) == 0 else sn[-1] - i
            sn.append(i)
        return (pre,nxt)
    def totalStrength(self, sth) -> int:
        n = len(sth)
        mod = 10**9+7
        @lru_cache(None) 
        def subArray(left,right,k):
            sm = 0
            for i in range(left,k):
                sm += sth[i]*(i-left+1)*(right-k+1)%mod
            for i in range(k,right+1):
                sm += sth[i]*(right-i+1)*(k-left+1)%mod
            return sm %mod
        pre,nxt =self.sumSubarrayMins(sth)
        #print(pre,nxt)
        ret = 0
        for i in range(n):
            tmp = sth[i] *subArray(i+1-pre[i],i-1+nxt[i],i)
            #print(tmp,i, i+1-pre[i],i-1+nxt[i],subArray(i+1-pre[i],i-1+nxt[i],i))
            ret +=tmp %mod
        #print(ret)
        return ret %mod
        
re = Solution().totalStrength([5,4,6])
print(re)