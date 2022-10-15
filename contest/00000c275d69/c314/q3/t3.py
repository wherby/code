

class Solution:
    def robotWithString(self, s: str) -> str:
        s=s +chr(ord("z")+1)
        ret =""
        n = len(s)
        pls = ["{"]*(n+1) 
        for i in range(n-1,-1,-1):
            pls[i] = min(pls[i+1],s[i])
        st =[]
        print(pls)
        for i,a in enumerate(s):
            while st and st[-1] <=pls[i]:
                ret = ret + st.pop()
            st.append(s[i])
        return ret




re =Solution().robotWithString("bdda")
print(re)