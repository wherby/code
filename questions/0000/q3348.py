


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        pls = [0]*4
        cur =int(t)
        ls = [2,3,5,7]
        for i,a in enumerate(ls):
            while cur%a ==0:
                pls[i] += 1
                cur = cur//a
        #print(cur,pls)
        if cur >1:
            return -1 

        dic = {}
        ls = [2,3,5,7]
        for i in range(1,10):
            tmp = [0]*4
            c =i 
            for j,a in enumerate(ls):
                while c%a ==0:
                    tmp[j] +=1
                    c = c//a 
            dic[i] = list(tmp)
        #print(dic) 
        n = len(num)
        def dfs(idx,state,cur):
            if  idx == n:
                for i,a in enumerate(state):
                    if a >0:
                        cur = cur + str(ls[i])*a
                return int(cur)
            res = 10**30
            for i in range(int(num[idx]),10):
                t1 = dic[i]
                ns = [a-b for a,b in zip(state,t1)]
                res = min(res,dfs(idx+1,ns,cur+str(i)))
            return res
        return dfs(0,pls,"")


re = Solution().smallestNumber(num = "1234", t = 256)
print(re)