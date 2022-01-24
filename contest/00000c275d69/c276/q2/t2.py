class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        sm =0
        cur = target
        while cur >1 and maxDoubles >0:
            if cur %2 ==1:
                sm +=1
                cur -=1
            else:
                cur = cur //2
                sm +=1
                maxDoubles -=1
        return sm + cur -1

re = Solution().minMoves(19,2)
print(re)
