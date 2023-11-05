class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ls = [0]*n
        for i in range(n):
            ls[i] = (i+1)%n
        #print(ls)
        last = -1 
        t = n-1
        idx = 0
        if k ==1:
            return n
        while t >0:
            m =k-1
            while m >0:
                last =ls[last]
                idx =ls[last]
                m -=1
            #print(last,idx)
            ls[last] = ls[idx]
            ls[idx] =-1
            t -=1
        #print(ls)
        for i,v in enumerate(ls):
            if v !=-1:
                return i+1

re =Solution().findTheWinner(n = 5, k = 2)