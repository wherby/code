# 设置状态参数g, 如果g 设立，说明已经大于，则从最小开始遍历，否则从当前值遍历， 然后做检验，如果不通过则回退
# 
from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n=len(s)
        cnt=Counter(s)
        odd=''
        t=0
        h=[0]*26
        for i in range(26):
            c=chr(97+i)
            v=cnt.get(c,0)
            if v%2: odd=c; t+=1
            h[i]=v//2
        if t>1: return ""
        m=n//2
        cur=[]
        def f(i,g):
            if i==m:
                half=''.join(cur)
                z=half+odd+half[::-1]
                return z if g or z>target else ""
            s0='a' if g else target[i]
            for u in range(ord(s0),123):
                j=u-97
                if h[j]:
                    cur.append(chr(u)); h[j]-=1
                    r=f(i+1,g or chr(u)>target[i])
                    if r: return r
                    h[j]+=1; cur.pop()
            return ""
        return f(0,False)