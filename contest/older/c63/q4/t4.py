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
            #print(left,right)
            if abs(left -right)< 0.1:
                return left
            mid = (left +right) *1.0 /2
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
            if cnt >k:
                right = mid
            elif cnt <k:
                left = mid
            else:
                left = mid
            return binarySearch(left,right)
        left= binarySearch(left,right)
        print(left)
        kt = k
        res = []
        for c in nums2:
            if c > 0:
                t =left /c if c !=0 else 0
                id = bisect_right(nums1,t)
                #print(id ,t,nums1,left,right)
                if id >0:
                    res.append(nums1[id -1] *c)
                    kt -= id-1
                else:
                    res.append(nums1[0] *c) 
            elif c <0:
                t =left /c if c !=0 else 0
                id = bisect_left(nums1,t)
                if id <len(nums1)-1:
                    res.append(nums1[id +1] *c)
                    kt -= len(nums1)- id 
                else:
                    res.append(nums1[-1] *c) 
        res = sorted(res)
        #print(res,kt)
        return res[kt-1]
            
                
        
        
nums1 = [-8,-8,3,7]


nums2 = [-1]
k = 3

re = Solution().kthSmallestProduct(nums1,nums2,k)
print(re)
