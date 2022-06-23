class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        mod = 10**9+7
        mn = nums[0]
        for i in range(n):
            if mn == nums[i]:continue
            if k <(i+1):break
            delta = nums[i] -mn
            if delta*(i) <k:
                k -= delta*(i)
                mn = nums[i]
            else:
                mn += k //(i)
                k = k %(i) 
                
                break
        for j in range(i):
            nums[j] = mn
        if k >=n:
            t = k //n 
            k= k-t*n
            for i in range(n):
                nums[i] += t
        idx = 0
        while k >0:
            nums[idx] +=1
            idx +=1
            k-=1
        ret = 1
        for a in nums:
            ret  = (ret*a) % mod
        return ret

re =Solution().maximumProduct(nums = [9,7,8], k = 9)
print(re)