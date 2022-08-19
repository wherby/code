
            
from importlib.resources import Package
from re import Pattern


class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        def getACC(ls):
            acc =0
            for a in ls:
                if a == "D":
                    acc +=1
                else:
                    acc -=1
            return acc
        n = len(pattern)
        mx = n+2
        dic ={}
        fd = False
        ret =[]
        def dfs(res,idx,last):
            nonlocal fd,ret
            if idx == n and  fd ==False:
                #print(res)
                fd = True
                ret = ""
                for a in res:
                    ret+=str(a)
                return res
            if idx ==n:
                return 
            if pattern[idx] =="I":
                for i in range(last+1,mx):
                    if i not in dic:
                        res.append(i)
                        dic[i] =1
                        dfs(res,idx +1,i)
                        del dic[i]
                        res.pop()
            else:
                for i in range(1,last):
                    if i not in dic:
                        res.append(i)
                        dic[i] =1
                        dfs(res,idx +1,i)
                        del dic[i]
                        res.pop()
        for i in range(1,10):
            dic={}
            res =[i]
            dic[i] =1
            dfs(res,0,i)
        return ret
        
        


re =Solution().smallestNumber("DDDIII")
print(re)