class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        ls = [0]*(n+1)
        lsr = [0]*(n+1)
        dic ={0:0}
        for i in range(n):
            ls[i+1] = ls[i]+ nums[i]
            lsr[n-i-1] = lsr[n-i] + nums[n-1-i]
            dic[lsr[n-1-i]] = i+1
        mx = 10**6
        #print(ls)
        for i in range(n+1):
            t = x - ls[i]
            if t in dic:
                t2 = i + dic[t] 
                mx = min(mx, t2)
                #print(t,dic[t],i)
        if mx ==10**6 or mx >n:
            return -1
        return mx

re = Solution().minOperations(nums = [1,1], x = 3)
print(re)