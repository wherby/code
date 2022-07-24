from bisect import bisect_right
class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 1
        dic = {}
        for a in rolls:
            dic[a] =1
            if len(dic) ==k:
                cnt +=1
                dic ={}
        return cnt         
                



re =Solution().shortestSequence(rolls =[1,3,3,2,1,4,1,1,2,4,1,2,2,1,1,1,1,2,2,3,4,3,3,2,1,4,4], k = 4)
#re =Solution().shortestSequence(rolls = [4,2,1,2,3,3,2,4,1], k = 4)

print(re)
