class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def verify(mid):
            left,right = 0,0
            if mid -2 - index >0:
                #print(mid -2 - index)
                left = (mid -2 -index) * (mid -1 -index ) //2 
            if mid - 2 -(n-index-1) >0:
                #print(mid - 1 -(n-index-1))
                right = (mid - 2 -(n-index-1)) *(mid  -1-(n-index-1))//2
            
            sm = n + (mid-1)* (mid -1) - left -right 
            #print(mid,left,right,sm)
            return sm <=maxSum
        l ,r = 0 ,10**10
        while l<r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid -1
        return l

re = Solution().maxValue(n = 3, index = 2,  maxSum = 18)
print(re)