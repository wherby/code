class Solution(object):
    def factorial(self,k):
        if k ==0 or k ==1:
            return 1
        else:
            return k * self.factorial(k-1)
            
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k=k-1
        res =[]
        nums = list([i for i in range(1,n+1)])
        for i in range(n-1,-1,-1):
            ith = self.factorial(i)
            m = k //ith
            res.append(nums[m])
            nums = nums[:m]+nums[m+1:]
            k = k - m*ith
        return "".join([str(i) for i in res])


        


print(Solution().getPermutation(3,3))
print(Solution().getPermutation(4,9))