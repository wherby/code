#https://leetcode.cn/problems/parse-lisp-expression/
from collections import defaultdict


class Solution:
    def evaluate(self, expression: str) -> int:
        i,n  = 0, len(expression)
        
        def parseVar():
            nonlocal i 
            i0 = i 
            while i <n and expression[i] != " " and expression[i] !=")":
                i +=1
            return expression[i0:i]
        def parseInt():
            nonlocal i 
            sign,x = 1,0
            if expression[i] == "-":
                sign = -1
                i +=1
            while i < n and expression[i].isdigit():
                x = x*10 + int(expression[i])
                i +=1
            return sign * x
        scope = defaultdict(list)
        
        def innerEvaluate():
            nonlocal i 
            if expression[i] != "(":
                if expression[i].islower():
                    return scope[parseVar()][-1]
                return parseInt()
            i +=1
            if expression[i] == "l":
                i +=4
                vars = []
                while True:
                    if not expression[i].islower():
                        ret = innerEvaluate()
                        break
                    var  = parseVar()
                    if expression[i] == ")":
                        ret = scope[var][-1]
                        break
                    vars.append(var)
                    i +=1
                    scope[var].append(innerEvaluate())
                    i +=1
                for var in vars:
                    scope[var].pop()
            elif expression[i] =="a":
                i+=4
                e1 = innerEvaluate()
                i +=1
                e2 = innerEvaluate()
                ret = e1 +e2
            else:
                i +=5
                e1 = innerEvaluate()
                i +=1
                e2 = innerEvaluate()
                ret = e1 *e2
            i+=1
            return ret
        return innerEvaluate()

re = Solution().evaluate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))")
print(re)