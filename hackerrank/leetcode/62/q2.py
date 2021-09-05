class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        inf = 1000000000000
        mx = [[inf]*(N+1) for _ in range(N+1)]
        
        for time in times:
            a,b,c = time[0],time[1],time[2]
            mx[a][b] = c

        d =[inf] *(N+1)
        d[K] =0
        p=[0]*(N+1)
        for i in range(1,N+1):
            zx =inf
            for j in range(1,N+1):
                if p[j]==0 and d[j] <zx:
                    zx = d[j]
                    k=j

            p[k]=1
            for j in range(1,N+1):
                if p[j] ==0 and mx[K][j] != inf and d[j] > d[K] + mx[K][j]:
                    d[j] = d[K] + mx[K][j]
        mxt= 0
        for i in range(1,N+1):
            t1 = d[i]
            if t1 > mxt:
                mxt=t1
        print d
        if mxt ==inf:
            return -1
        return mxt



s = Solution()
times=[[2,1,1],[2,3,1],[3,4,1]]

print s.networkDelayTime(times,4,2)
