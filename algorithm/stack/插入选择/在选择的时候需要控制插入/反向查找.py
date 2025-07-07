# 用可以作为选择的时间作为指针，插入对应candidate，在里面选择最小的右边界
import heapq
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x:x[0])
        cnt = 0
        st =[]
        idx = 0
        n = len(events)
        #print(events)
        for i in range(1,10**5+1):
            while idx < n and events[idx][0]<= i:
                k = events[idx]
                idx +=1
                heapq.heappush(st, (k[1],k[0]))
            #print(st)
            while st  and st[0][0]< i:
                #print(st,i)
                heapq.heappop(st)
            if st:
                heapq.heappop(st)
                cnt +=1
            #print(st,i)
        return cnt

re = Solution().maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])
print(re)