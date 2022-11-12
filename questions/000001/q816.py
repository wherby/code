from typing import List, Tuple, Optional

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        st1 = s[1:len(s)-1]
        n = len(st1)
        def verify(s):
            if len(s) >1 and s[0] ==s[-1] == "0":
                return False
            return True
        st = []
        def setPoint(s):
            
            m = len(s)
            if m ==1:
                return [s]
            if m >1 and s[0]=="0":
                ret =[]
            else:
                ret  =[s]
            if s[-1] =="0" or m ==1:
                return ret
            if s[0] == "0" and m>1:
                ret.append(s[0] + "." +s[1:])
                return ret
            for j in range(1,m):
                ret.append(s[:j] + "." + s[j:])
            return ret
            
        for i in range(1,n):
            ls1,ls2 = st1[:i],st1[i:]
            if not verify(s)  or not verify(s): continue
            l1 = setPoint(ls1)
            l2 = setPoint(ls2)
            for a in l1:
                for b in l2:
                    st.append("(" + a + ", " +b +")")
        return st

re =Solution().ambiguousCoordinates( "(100)")
print(re)

