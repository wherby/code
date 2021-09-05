#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m =len(nums1)
        n = len(nums2)
        if m>n:
            n,m,nums1,nums2 = m,n,nums2,nums1
        imin =0
        imax = m
        halfLen = (m+n +1) /2

        while imin <= imax:
            i = (imin + imax)/2
            j = halfLen - i
            if i < m and nums2[j-1] > nums1[i]:
                imin =i+1
            elif i > 0 and  nums1[i-1] >nums2[j]:
                imax =i -1
            else:
                if  i ==0:
                    maxLeft = nums2[j-1]
                elif j ==0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1],nums2[j-1])

                if (m+n)%2 ==1:
                    return maxLeft
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i],nums2[j])
                return (minRight + maxLeft) /2.0

        



nums1 = [1, 3]
nums2 = [2]
s = Solution()
print s.findMedianSortedArrays(nums1,nums2)