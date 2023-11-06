from bisect import bisect_left
class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        minls =[-nums1[0]]*n
        for i in range(1,n):
            minls[i] = max(minls[i-1],-nums1[i])
       
        mn=0
        for i, num in enumerate(nums2):
            idx= bisect_left(minls,-num)
            #print(idx,-num,i)
            if idx < n:
                mn = max(mn,i-idx)
        #print(minls)
        return mn

re =Solution().maxDistance(nums1 = [2,2,2], nums2 = [10,10,1])
print(re)

