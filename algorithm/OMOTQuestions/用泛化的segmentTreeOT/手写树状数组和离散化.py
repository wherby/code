# 离散化值域和手写BIT
# 2.8s
class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        val = sorted(set(nums))
        m = len(val)
        rank = {v:i+1 for i, v in enumerate(val)}
        bitdown = [0]*(m+2)
        bitup = [0] * (m+2)
        def upda(bi, i, va):
            while i <=m:
                if va>bi[i]:
                    bi[i] = va
                i += i & -i
        def que(bi, i):
            res = 0
            while i>0:
                if bi[i]>res:
                    res = bi[i]
                i -= i & -i
            return res
        n = len(nums)
        dpup = [0]*n
        dpdown = [0]*n
        temp = 0
        for i in range(n):
            if i>=k:
                j=i-k
                vj = nums[j]
                rj = rank[vj]
                upda(bitdown, rj,dpdown[j])
                revj = m-rj+1
                upda(bitup, revj,dpup[j])
            v = nums[i]
            r = rank[v]
            bedown = que(bitdown, r-1)
            dpup[i] = v + bedown
            beup = que(bitup, m-r)
            dpdown[i] = v + beup
    
            if dpup[i]>temp:
                temp = dpup[i]
            if dpdown[i]>temp:
                temp = dpdown[i]
    
        return temp
        