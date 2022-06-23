import heapq
class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        """
        :type flowers: List[List[int]]
        :type persons: List[int]
        :rtype: List[int]
        """
        st =[]
        for x,y in flowers:
            st.append((x,1))
            st.append((y+1,-1))
        heapq.heapify(st)
        querys = []
        n = len(persons)
        for i,t in enumerate(persons):
            querys.append((t,i))
        querys.sort()
        ret = [0]*n
        acc =0
        to =0
        idx =0
        last = -1
        #print(st,querys)
        while st:
            to,dif =heapq.heappop(st)
            while idx < n and querys[idx][0]<to:
                ret[querys[idx][1]] = acc
                idx +=1
            last = to 
            acc += dif
            while st and last ==st[0]:
                to,dif = heapq.heappop(st)
                acc += dif
                last = to
                #print("1")

            #print(st,acc,ret)
        return ret

re = Solution().fullBloomFlowers(flowers = [[1,10],[3,3]], persons = [3,3,2])
print(re)
                
        