# https://leetcode-cn.com/problems/maximum-subarray-min-product/
class Solution(object):
    def maxSumMinProduct(self, nums):
        n = len(nums)
        pre = [nums[0]]*n
        for i in range(1,n):
            pre[i] = pre[i-1]+ nums[i]
        preSmaller =[-1]*n
        nextSmaller =[n]*n
        q =[]
        for i in range(n):
            while q and nums[q[-1]]> nums[i]:
                nextSmaller[q[-1]] = i
                q.pop()
            q.append(i)
        q=[]
        for i in range(n-1,-1,-1):
            while q and nums[q[-1]]> nums[i]:
                preSmaller[q[-1]] = i
                q.pop()
            q.append(i)
        #print(preSmaller,nextSmaller)
        mx =0
        for i in range(n):
            a = preSmaller[i]
            b = nextSmaller[i]
            pa = pre[a] if a != -1 else 0
            sm = pre[b-1] - pa
            mx = max(mx, sm * nums[i])
        return mx%(10**9+7)
    