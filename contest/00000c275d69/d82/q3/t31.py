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
        ls.sort()
        ls = [0]+ ls
        k  = k1 +k2
        pls =[0]*(n+1)
        sm = sum(ls)
        for i in range(n+1):
            pls[i] = pls[i-1] + ls[i]
        acc =0
        for i in range(n,-1,-1):
            if acc >=k:
                break
            acc += (ls[i] - ls[i-1])*(n-i+1)
        ret = ls[1:i+1]
        remains =sm-k - pls[i]
        if remains <=0:
            remains =0
        for j in range(i+1,n+1):
            k = n -j +1
            ret.append(remains//k)
            remains -= remains//k
        ans = 0
        for a in ret:
            ans += a*a
        return ans
        




re =Solution().minSumSquareDiff([10,10,10,11,5],[1,0,6,6,1],11,27)
print(re)