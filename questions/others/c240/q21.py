class Solution(object):
    def maxDistance(self, nums1, nums2):
        n ,m = len(nums1),len(nums2)
        i,j =0,0
        while i<n and j <m:
            if nums1[i]>nums2[j]:
                i +=1
            j +=1
        return j -i-1 if j-i-1>=0 else 0