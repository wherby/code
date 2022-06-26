class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        def maxSubArray(ls):
            mx =0
            t =0 
            for a in ls:
                t += a 
                if t >0:
                    mx= max(mx,t)
                else:
                    t =0
            return mx
        def getMax(nums1,nums2):
            ls =[0]*n
            for i in range(n):
                ls[i] = nums1[i] - nums2[i]
            ret = sum(nums2)
            #print(ret, maxSubArray(ls),ls)
            return ret + maxSubArray(ls)
        return max(getMax(nums1,nums2),getMax(nums2,nums1))
    
re =Solution().maximumsSplicedArray([10,20,50,15,30,10],[40,20,10,100,10,10])
print(re)