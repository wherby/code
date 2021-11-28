class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        n = len(nums)
        idxmn,idxmx =-1 ,-1
        for i,a in enumerate(nums):
            if a == mn:
                idxmn =i
            if a == mx :
                idxmx =i
        if idxmn > idxmx:
            idxmn,idxmx = idxmx,idxmn
        a1 =idxmx +1
        a2 =n-idxmn
        a3 = idxmn +1 + n -idxmx
        return min(a1,a2,a3)
