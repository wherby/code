# https://leetcode.com/contest/biweekly-contest-63/problems/kth-smallest-product-of-two-sorted-arrays/
# kth item using binary search and for >0 , <0 ,==0 
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        res =[]
        for i in nums1:
            res.append(i* nums2[0])
        for j in nums2:
            res.append(j * nums1[0])
        
        for i in nums1:
            res.append(i* nums2[-1])
        for j in nums2:
            res.append(j * nums1[-1])
        left = min(res)
        right =max(res)

        def binarySearch(left,right):
            if left == right:
                return left
            #print(left,right)
            mid = (left +right)  //2
            cnt = 0
            for c in nums2:
                if c > 0:
                    t =mid /c if c !=0 else 0
                    id = bisect_right(nums1,t)
                    #print(id ,t,nums1,left,right)
                    cnt +=id
                elif c <0:
                    t =mid /c if c !=0 else 0
                    id = bisect_left(nums1,t)
                    cnt +=len(nums1) - id 
                else:
                    if mid >=0:
                        cnt += len(nums1)
            #print(cnt)
            #print(left,right,mid,cnt,k)
            if cnt <k:
                left = mid+1
            else:
                right = mid
            return binarySearch(left,right)
        left= binarySearch(left,right)
        print(left)
        return left
        #print(res,kt)
        #return res[kt-1]
        