from bisect import bisect_right,bisect_left
from sortedcontainers import SortedList

class DiscreteMax():
    def __init__(self):
        self.ls=SortedList([(0,0)])
    
    def insert(self, idx,val):
        k = bisect_left(self.ls,(idx,0))
        if k == len(self.ls):
            if val >self.ls[-1][1]:
                self.ls.add((idx,val))
        else:
            if val >self.ls[k-1][1]:
                removed=[]
                for i in range(k,len(self.ls)):
                    if val > self.ls[i][1]:
                        removed.append(self.ls[i])
                #print(removed,k)
                for item in removed:
                    self.ls.remove(item)
                self.ls.add((idx,val))
    
    def query(self,idx):
        k = bisect_right(self.ls,(idx,10**19))
        return self.ls[k-1][1]

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dm =DiscreteMax()
        for i in range(n):
            pr,cs = questions[i]
            dm.insert(i + cs +1,dm.query(i) + pr)
        return dm.query(n + 10**10)

re = Solution().mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])
print(re)