class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b = b,a %b
            return a
        g = numsDivide[0]
        for a in numsDivide:
            g = gcd(g,a)
        nums.sort()
        for i,a in enumerate(nums):
            if gcd(a,g) ==a:
                return i
        return -1




re =Solution()
print(re)