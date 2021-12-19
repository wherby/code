## ?????
class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def allState(k):
            m=n
            state = (1<<k) -1
            while (state <(1<<m)):
                for j in range(n):
                    if (state>>j) & 1 :
                        dp1[state] = min(dp1[state],dp2[state - (1<<j)] + (nums1[j] ^ nums2[i]) )
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
        mn = 10**19
        n = len(nums1)
        dp1 = [mn] * (1<<n)
        dp2 = []
        dp1[0] =0
        for i in range(n):
            dp2 = list(dp1) # deep copy
            allState(i+1)
        return dp1[(1<<n) -1]

#re = Solution().minimumXORSum([9606269,5221932,7334481,8439484,5986425,8864979,5430580,14172,2078710,7420803,7542233],[5875595,5113681,9047874,6700866,5693602,9586753,8259408,1897425,6334375,6415366,3421110])
#re = Solution().minimumXORSum([1,0,3],[5,3,4])
re = Solution().minimumXORSum(nums1 = [1,2], nums2 = [2,3])
print(re)