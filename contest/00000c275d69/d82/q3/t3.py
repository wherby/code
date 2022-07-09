def arrayChangeWithK(ls,k):
    left,right = 0,10**11
    count =0
    while left < right:
        mid = (left+right)>>1
        sm = 0
        for a in ls:
            sm += max(0, a -mid )
        if sm >k:
            left = mid +1
        else:
            right = mid 
            count = k - sm 
    ret= []
    if left ==0:
        return [0]*len(ls)
    for a in ls:
        if a < left:
            ret.append(a)
        else:
            ret.append(left -min(1,max(0,count)))
            count -=1
    return ret

class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        ls = [0]*n
        for i in range(n):
            ls[i] = abs(nums1[i] -nums2[i])
        k  =k1 +k2
        ls = arrayChangeWithK(ls,k)
        ans =0
        for a in ls:
            ans += a**2
        return ans
        




re =Solution().minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0)
print(re)