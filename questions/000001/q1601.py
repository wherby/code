class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        
        sm = 0
        m = len(requests)
        def check(state):
            ls = [0]*21
            for i in range(m):
                if (1<<i) & state != 0:
                    f,t = requests[i]
                    ls[f] -=1
                    ls[t] +=1
            for i in range(21):
                if ls[i] != 0:
                    return False
            return True
        def allState(k):
            state = (1<<k) -1
            while (state <(1<<m)):
                if check(state):
                    return k
                c = state &(-state)
                r = state +c
                state= (((r ^ state) >>2)//c) |r 
            return -1
        for k in range(m,-1,-1):
            re =  allState(k)
            if re != -1:
                return re
        return 0

re = Solution().maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]])
print(re)