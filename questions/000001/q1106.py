class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        tmp=[]
        ls = []
        for a in expression[::-1]:
            if a ==",":continue
            if a =="(":continue
            if a == ")":ls.append(")")
            if a =="!":
                k = ls.pop()
                ls.pop()
                ls.append(not k)
            if a == "f":
                ls.append(False)
            if a == "t":
                ls.append(True)
            if a =="&":
                tmp =[]
                while ls[-1]  != ")":
                    tmp.append(ls[-1])
                    ls.pop()
                ls.pop()
                k = tmp
                k = all(k)
                ls.append(k)
            if a == "|":
                tmp =[]
                while ls[-1]  != ")":
                    tmp.append(ls[-1])
                    ls.pop()
                ls.pop()
                k = tmp
                k = any(k)
                ls.append(k)
        return ls[0]

re =Solution().parseBoolExpr("|(&(t,f,t),!(t))")