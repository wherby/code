# https://leetcode.cn/problems/make-sum-divisible-by-p/submissions/

class Solution:
    def minSubarray(self, nums, p: int) -> int:
        x = sum(nums)%p
        if x ==0:
            return 0 
        acc = 0
        dic = {}
        dic[0]=-1
        n = len(nums)
        mx= n
        for i,a in enumerate(nums):
            acc =(acc+a)%p 
            if (acc-x)%p in dic:
                mx = min(mx, i - dic[(acc-x)%p])
            dic[acc] = i 
        return mx if mx != n else -1 