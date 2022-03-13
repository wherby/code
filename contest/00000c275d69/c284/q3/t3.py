class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) ==1 and k %2==1:
            return -1
        
        if k == 0:
            return nums[0]
        n = len(nums)
        mx1 =0
        if n > k:
            mx1 = nums[k]
        mx2 = 0
        if k >1 and k < n :
            t = min(n,k-1)
            mx2 = max(nums[:t])
        elif k >=n:
            if k==n:
                t = min(n-1,k-1)
                #print(t)
                mx2 = max(nums[:t])
            else:
                t = min(n,k-1)
                mx2 = max(nums[:t])
        #print(mx1,mx2)
        return max(mx1,mx2)

re = Solution().maximumTop([3,1],4)
print(re)