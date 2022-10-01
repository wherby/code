# https://leetcode.com/contest/biweekly-contest-63/problems/kth-smallest-product-of-two-sorted-arrays/
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        def verify(mid):
            cnt =0 
            for a in nums1:
                if a > 0 :
                    k = bisect_right(nums2,mid/a)
                    cnt += k
                elif a <0:
                    k = bisect_left(nums2,mid/a)
                    cnt += len(nums2) -k 
                else:
                    if mid >=0:
                        cnt += len(nums2)
            return cnt
        res =[]
        for i in nums1:
            res.append(i* nums2[0])
        for j in nums2:
            res.append(j * nums1[0])
        
        for i in nums1:
            res.append(i* nums2[-1])
        for j in nums2:
            res.append(j * nums1[-1])
        l = min(res)
        r =max(res)
        # l,r = -10**10,10**10 This setting will timeout
        while l < r :
            mid = (l+r)>>1
            if verify(mid) <k:
                l = mid +1 
            else:
                r =mid 
        return l

re = Solution().kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3)
print(re)