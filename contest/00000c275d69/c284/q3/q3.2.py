class Solution(object):
    def maximumTop(self, nums, k):
        n = len(nums)
        if n ==1 and k &1:
            return -1
        l = [(nums[i],i) for i in range(n)]
        l.sort(reverse= True)
        for v,i in l:
            if i > k:
                continue
            if i == k-1:
                continue
            return v
        return -1