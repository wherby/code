class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def verify(ls):
            ls.sort()
            n = len(ls)
            if n<=2:
                return True
            for i in range(1,n):
                if ls[i] - ls[i-1] != ls[1]-ls[0]:
                    return False
            return True
        p = zip(l,r)
        res =[]
        for l,r in p:
            tp = list(nums[l:r+1])
            res.append(verify(tp))
        return res

re = Solution().checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
print(re)
