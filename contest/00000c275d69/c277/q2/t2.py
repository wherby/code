class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pls =[]
        nls= []
        for a in nums:
            if a >0:
                pls.append(a)
            else:
                nls.append(a)
        res =[]
        n = len(pls)
        for i in range(n):
            res.append(pls[i])
            res.append(nls[i])
        return res