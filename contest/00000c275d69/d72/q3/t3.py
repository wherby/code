import re


class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum%2 ==1:
            return []
        res =[]
        idx = 2
        while finalSum >= idx:
            if finalSum- idx <= idx:
               res.append(finalSum)
               finalSum =0
            else:
                res.append(idx)
                finalSum -= idx
                idx +=2
        return res

re = Solution().maximumEvenSplit(2)
print(re)