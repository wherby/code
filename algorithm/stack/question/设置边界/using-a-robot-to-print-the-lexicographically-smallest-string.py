# https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/submissions/371158357/
# 这路设置了一个弹出堆栈的边界值
class Solution:
    def robotWithString(self, s: str) -> str:
        s=s +chr(ord("z")+1)
        ret =""
        n = len(s)
        pls = ["{"]*(n+1) 
        for i in range(n-1,-1,-1):
            pls[i] = min(pls[i+1],s[i])
        st =[]
        for i,a in enumerate(s):
            while st and st[-1] <=pls[i]:
                ret = ret + st.pop()
            st.append(s[i])
        return ret