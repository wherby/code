from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events=sorted(events)
        #print(events)
        e2 = []
        start =[]
        smx = 0
        for e in events:
            start.append(e[0])
            e2.append([e[1],e[0],e[2]])
            smx =max(smx , e[2])
        e2 = sorted(e2)
        mx =0
        n = len(events)
        for i in range(n):
            e = events[n-1-i]
            #print(e)
            mx =max(mx,e[2])
            e[2] = mx
        mx =0
        for e in e2:
            #print(e)
            mx =max(mx,e[2])
            e[2]= mx
        res =smx
        k = 0
        k2 =0
        #print(e2,events,start)
        
        for s in start:
            #print(s)
            while  k <n and  e2[k][0] <s :
                k +=1
            while k2 <n and  events[k2][0]<=s :
                k2 +=1
            #print(k,k2,s)
            if k != 0 :
                res =max(res,e2[k-1][2]+events[k2-1][2])
        return res
        

events = [[1,3,2],[4,5,2],[1,5,5]]
re =Solution().maxTwoEvents(events)
print(re)