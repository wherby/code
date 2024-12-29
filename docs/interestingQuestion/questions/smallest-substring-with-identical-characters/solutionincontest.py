# https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/solutions/3027031/er-fen-da-an-tan-xin-gou-zao-pythonjavac-3i4f/
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        s = [int(a) for a in s]
        def getN(s,numOps):
            n = len(s)
            
            def verify(mid):
                state = 1
                lstV = s[0]
                cnt =0
                for i in range(1,n):
                    if s[i] == lstV:
                        state +=1
                        if state>mid:
                            state=1
                            lstV = 1- lstV
                            if mid==2 and i<n-1 and s[i+1] ==lstV:
                                lstV = 1-lstV
                            cnt +=1
                            if cnt >numOps:
                                return False
                    else:
                        lstV = s[i]
                        state =1
                return True
            l,r =1,n
            while l<r:
                mid = (l+r)>>1
                if verify(mid):
                    r=mid 
                else:
                    l= mid+1
            return l
        
        ret = min(getN(s,numOps),getN(s[::-1],numOps))
        if numOps >0:
            s1= list(s)
            s1[0] = 1- s1[0]
            s2 = list(s)[::-1]
            s2[0] = 1 -s2[0]
            numOps -=1
            ret =min(ret,getN(s1,numOps),getN(s2,numOps))
        return ret