from collections import defaultdict,deque
class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ls= [0]*n
        self.dic = defaultdict(list)
        self.n = n

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        n = self.n
        pls = [0]*(n+1)
        for i in range(n):
            pls[i+1]= pls[i] + self.ls[i]
        for i in range(self.n-size+1):
            if pls[i+size]-pls[i] ==0:
                for j in range(size):
                    self.dic[mID].append(j+i)
                    self.ls[i+j] = mID
                return i 
        return -1


    def free(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        cnt = len(self.dic[mID])
        for j in self.dic[mID]:
            self.ls[j]=0
        self.dic[mID]=[]
        return cnt
