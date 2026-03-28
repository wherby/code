# https://leetcode.cn/problems/count-good-subarrays/submissions/710415641/

class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        ans = 0
        lps = {} 
        rds = []  
        
        for i, x in enumerate(nums):
            lps[x] = i
            nrds = []
            curr_val, curr_idx = x, i
            
            for v, l in rds:
                combined = v | x
                if combined == curr_val:
                    curr_idx = l
                else:
                    nrds.append((curr_val, curr_idx))
                    curr_val, curr_idx = combined, l
            nrds.append((curr_val, curr_idx))
            rds = nrds

            for val, left in rds:
                if val in lps and lps[val] >= left:
                    ans += (lps[val] -left + 1)
        return ans





re =Solution().countGoodSubarrays([10,6,4,2])
print(re)