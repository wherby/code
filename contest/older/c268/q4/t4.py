class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def isMirror(ls):
            if len(ls)==1:
                return True
            m = len(ls)
            for i in range(m):
                if ls[i] != ls[m-1-i]:
                    return False
            return True
        def toK(x):
            ls = []
            while x >0:
                t = x %k
                ls.append(t)
                x = x //k 
            return ls
        def getMirror(ls):
            nextCand =[]
            tood=[]
            teven =[]
            for l in ls:
                for j in range(10):
                    nextCand.append(l*10 +j )
                    tood.append(int(str(l) +str(j) +str(l)[::-1]))
                    teven.append(int(str(l) +str(j) +str(j) +str(l)[::-1]))
            return tood + teven,nextCand
        nextCand =list(range(1,10))
         
        #nextV,nextCand =getMirror(nextCand)
        cand = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
        cnt= 0
        res =0
        while cnt < n:
            for c in cand:
                isM = isMirror(toK(c))
                if isM:
                    cnt +=1
                    res +=c
                    if cnt == n :
                        return res
            cand,nextCand= getMirror(nextCand)

re =Solution().kMirror(3,7)
print(re)