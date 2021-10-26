#https://leetcode-cn.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
import functools
class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        def fadd(a,b):
            return a^b
        a1 = functools.reduce(fadd,arr1)
        a2 = functools.reduce(fadd,arr2)
        return a1&a2

arr1 = [1,2,3]
arr2 = [6,5]
re =Solution().getXORSum(arr1,arr2)
print(re)