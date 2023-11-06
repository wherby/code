import heapq
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        vAndL = zip(values,labels)
        ls = []
        dic ={}
        for v,l in vAndL:
            heapq.heappush(ls,(-v,l))
            dic[l] =useLimit
        sm = 0
        while ls and  numWanted >0:
            v,l= heapq.heappop(ls)
            if dic[l] >0:
                sm -= v 
                dic[l] -=1
                numWanted -=1
        return sm
re = Solution().largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2)
print(re)
