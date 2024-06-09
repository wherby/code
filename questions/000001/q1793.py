from typing import List, Tuple, Optional

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = k,k 
        lmn,rmn = nums[k], nums[k]
        ret = nums[k]
        mn = nums[k]
        while l != 0 or r != n-1:
            while l >0 and nums[l-1] >= mn:
                l -=1 
            while r < n-1 and nums[r+1] >= mn:
                r +=1 
            ret = max(ret, (r-l+1)*mn)
            
            if l >0 and r < n-1:
                if nums[l-1]>= nums[r+1]:
                    l-=1 
                    lmn = min(lmn,nums[l])
                    mn = min(lmn,mn)
                else:
                    r +=1
                    rmn = min(rmn,nums[r])
                    mn = min(mn,rmn)
            elif l ==0 and r < n-1:
                r +=1 
                rmn = min(rmn,nums[r])
                mn = min(mn,rmn)
            elif r == n-1 and l >0:
                l -=1 
                lmn = min(lmn,nums[l])
                mn = min(mn,lmn)
            ret = max(ret,(r-l+1)*mn)
        return ret

re = Solution().maximumScore(nums = [8182,1273,9847,6230,52,1467,6062,726,4852,4507,2460,2041,500,1025,5524], k = 8)
print(re)
            