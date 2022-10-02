class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        acc =0
        m,n = len(nums1),len(nums2)
        if m %2 ==1:
            for a in nums2:
                acc = acc ^a 
        if n %2 ==1:
            for a in nums1:
                acc =acc ^a 
        return acc





re =Solution().xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0])
print(re)