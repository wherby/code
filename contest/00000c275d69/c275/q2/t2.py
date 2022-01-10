class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        c1 = 0
        for a in nums:
            if a == 1:
                c1+=1
        tls =[0]* n 
        for i in range(n):
            tls[i] = tls[i-1] + nums[i]
        tls2 = [0]*n*2
        for i in range(n):
            tls2[i] = tls[i]
            tls2[n+i] = tls[-1] + tls[i]
        tls2 =[0]+ tls2
        mx = n
        #print(tls2)
        for i in range(n):
            j = i + c1 
            k = c1 -(tls2[j]- tls2[i])
            #print(c1,tls2[j-1],tls2[i],j-1,i,c1-(tls2[j-1]- tls2[i]))
            mx = min(mx,k)
        return mx

re = Solution().minSwaps(nums = [0,1,0,1,1,0,0])
print(re)