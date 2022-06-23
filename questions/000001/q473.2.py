#https://leetcode.cn/problems/matchsticks-to-square/
class Solution:
    def makesquare(self, mats) -> bool:
        n = len(mats)
        mats.sort(reverse =True)
        if sum(mats)%4 != 0:
            return False
        k = sum(mats) //4
        def add(s):
            sm =[]
            for i in range(n):
                if (1<<i) & s:
                    sm.append(mats[i])
            return sm
        fd = False

        dic ={}
        
        cand = []
        for i in range(1<<n):
            if sum(add(i)) ==k:
                cand.append(i)
        
        def dfs(s):
            nonlocal fd
            if s == (1<<n)-1:
                fd = True
            for j in cand:
                if s &j ==0:
                    st =add(j)
                    if (s,tuple(st)) not in dic and sum(st)==k:
                        dic[(s,tuple(st))] =1
                        dfs(s+j)
            return fd
        dfs(0)
        return fd 

re = Solution().makesquare([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(re)
                    