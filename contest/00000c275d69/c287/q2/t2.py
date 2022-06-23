from collections import defaultdict
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        dic1 = defaultdict(int)
        for w,l in matches:
            dic1[l] +=1
        winner =[]
        loser=[]
        dic={}
        for w,l in matches:
            if w not in dic1 and w not in dic:
                winner.append(w)
                dic[w] =1
            if dic1[l] ==1 and l not in dic:
                loser.append(l)
                dic[l]=1
        winner.sort()
        loser.sort()
        return [winner,loser]

re = Solution().findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
print(re)