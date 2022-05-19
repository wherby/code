class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def fd(x):
            cnt =0
            for i in range(1,n+1):
                cnt += min(x // i,m) 
            if cnt <k:
                return False
            else:
                return True
        l,r = 1,m*n
        while l <r:
            mid = (l+r)>>1
            if fd(mid)==False:
                l = mid +1
            else:
                r = mid
        return l 

re = Solution().findKthNumber(2,3,6)
print(re)