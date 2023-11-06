from bisect import bisect_right
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        n = len(nums1)
        smV =0
        for i in range(n):
            smV += abs(nums1[i] - nums2[i])
        dif =0
        sls = list(nums1)
        sls.sort()
        for i in range(n):
            t = nums2[i]
            k = bisect_right(sls,t)
            #print(t,k)
            if k == 0:
                gain = abs(nums1[i] - nums2[i]) - abs(sls[0] -nums2[i])
                dif = max(dif,gain)
            elif k == n :
                gain =  abs(nums1[i] - nums2[i]) -abs(sls[n-1]- nums2[i])
                dif = max(dif,gain)
                #print(dif,gain,t, sls[n-1],sls)
            else:
                gain =  abs(nums1[i] - nums2[i]) -abs(sls[k] - t)
                gain2 =abs(nums1[i] - nums2[i]) -abs(sls[k-1]-t)
                dif  = max(gain,gain2,dif)
        #print(dif)
        smV -= dif
        return smV % (10**9+7)

re =Solution().minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4])
print(re)
