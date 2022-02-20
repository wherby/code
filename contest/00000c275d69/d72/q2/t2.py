class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3 !=0:
            return []
        k = num //3
        return [k-1,k,k+1]