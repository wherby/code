class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls =[]
        def getCount(i,n):
            t = i
            cnt =0
            while cnt ==0 or t !=i:
                if t %2 ==0:
                    t =t//2
                else:
                    t = n//2 + (t-1)//2
                cnt +=1
            return cnt
        mn =0
        for i in range(n):
            r = getCount(i,n)
            print(r)
            mn = max(mn,r)
        return mn

re = Solution().reinitializePermutation(22)