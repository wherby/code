class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm = sum(nums)
        pre =[0]*(len(nums)+1)
        for i,a in enumerate(nums):
            pre[i+1] = pre[i]+a
        mn = 10**9
        idx =0
        n = len(nums)
        for i in range(len(nums)):
            left = pre[i+1] //(i+1)
            right = (sm - pre[i+1]) // (n-i-1) if i !=n-1 else 0
            tp = abs(right-left)
            if tp < mn:
                mn = tp
                idx =i
                #print(idx,mn,left,right)
        return idx
re = Solution().minimumAverageDifference(nums = [2,5,3,9,5,3])
print(re)