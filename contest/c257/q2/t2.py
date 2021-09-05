import heapq
class Solution:
    def numberOfWeakCharacters(self, properties) :
        if len(properties) <2:
            return 0
        ls = sorted(properties)
        send = [[] for i in range(100001)]
        for t in ls:
            #print(t)
            send[t[0]].append(t[1])
        #print(send[:10])
        st=[100000000000]
        cnt =0
        for tp in send:
            if len(tp) >0:
                #print(st,tp,cnt)
                mx = max(tp)
                #print(mx)
                while st[0] < mx:
                    cnt +=1
                    heapq.heappop(st)
                for t in tp:
                    heapq.heappush(st,t)
        return cnt




properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
re = Solution().numberOfWeakCharacters(properties)
print(re)