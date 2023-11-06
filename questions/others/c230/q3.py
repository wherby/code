class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        
        sm1, sm2 = sum(nums1),sum(nums2)
        if sm1 > sm2:
            nums1,nums2 = nums2,nums1
        sm1, sm2 = sum(nums1),sum(nums2)
        n,m = len(nums1), len(nums2)
        diff = sm2 - sm1
        cnt =0
        idx1 = 0
        idx2 = m-1 
        while diff >0:
            if idx1 == n:
                if idx2 == -1:
                    return -1
                if nums2[idx2]>1:
                    t = nums2[idx2] -1
                    diff -=t
                    cnt +=1
                    idx2 -=1
                else:
                    idx2 -=1
            if idx2 == -1:
                if idx1 == n:
                    return -1
                if nums1[idx1] < 6:
                    t = 6 - nums1[idx1]
                    diff -= t
                    cnt +=1
                    idx1  +=1
                else:
                    idx1 +=1
           
            #print(idx1,idx2)
            if idx1 !=n and idx2 !=-1 and 6- nums1[idx1] > nums2[idx2] -1:
                t = 6 - nums1[idx1]
                diff -= t
                cnt +=1
                idx1  +=1
            elif idx1 !=n and idx2 !=-1 :
                t = nums2[idx2] -1
                diff -=t
                cnt +=1
                idx2 -=1
        return cnt 

re = Solution().minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6])
print(re)