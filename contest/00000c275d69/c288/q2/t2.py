class Solution:
    def minimizeResult(self, expression: str) -> str:
        a,b = expression.split("+")
        m,n = len(a),len(b)
        mx = int(a) +int(b)
        res ="("+ expression +")"
        def getV(s1):
            if len(s1) ==0:
                return 1
            return int(s1)
        for i in range(m):
            for j in range(1,n+1):
                a1 =getV(a[:i])
                a2 =getV(a[i:])
                b1 = getV(b[:j])
                b2 =getV(b[j:])
                ret = a1*(a2+b1)*b2
                if ret < mx:
                    mx = ret
                    res = a[:i]+"(" +a[i:] + "+" + b[:j] + ")" + b[j:]
        return res


re = Solution().minimizeResult("999+999")
print(re)