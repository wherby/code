class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        left, idxMn,idxmx = -1,-1,-1
        cnt = 0
        for i,a in enumerate(nums):
            if a == minK:
                idxMn= i 
            if a == maxK: idxmx = i 
            if a < minK or a > maxK: left = i 
            cnt  += max(0, min(idxMn,idxmx) - left)
        return cnt
        
re =Solution().countSubarrays([978650,978650,978650,68071,52201,68071,186141,978650,978650,267135,68071,717241,242895,68071,582505,978650,68071,68071],68071,978650)
print(re)