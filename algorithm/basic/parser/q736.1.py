
from collections import defaultdict
from enum import Enum, auto


class ExprStatus(Enum):
    VALUE = auto()
    NONE = auto()
    LET = auto()
    LET1 = auto()
    LET2 = auto()
    ADD = auto()
    ADD1 = auto()
    ADD2 = auto()
    MULT = auto()
    MULT1 = auto()
    MULT2 = auto()
    DONE =auto()

class Expr:
    __slot__ = 'status','var','value','e1','e2'
    
    def __init__(self,status) -> None:
        self.status = status
        self.var = ""
        self.value = 0
        self.e1=self.e2 =0

class Solution:
    def evaluate(self, expression: str) -> int:
        scope = defaultdict(list)
        
        def calculateToken(token):
            return scope[token][-1] if token[0].islower() else int(token)

        vars = []
        s = []
        cur  = Expr(ExprStatus.VALUE)
        i,n = 0, len(expression)
        while i < n :
            if expression[i] == " ":
                i +=1
                continue
            if expression[i] == "(":
                i +=1
                s.append(cur)
                cur = Expr(ExprStatus.NONE)
                continue
            if expression[i] == ")":
                i +=1
                if cur.status is ExprStatus.LET2:
                    token = str(cur.value)
                    for var in vars[-1]:
                        scope[var].pop()
                    vars.pop()
                elif cur.status is ExprStatus.ADD2:
                    token = str(cur.e1 + cur.e2)
                else:
                    token = str(cur.e1 * cur.e2)
                cur = s.pop()
            else:
                i0 = i
                while i < n and expression[i] != " " and expression[i] != ")":
                    i +=1
                token = expression[i0:i]
            
            if cur.status is ExprStatus.VALUE:
                cur.value = int(token)
                cur.status =ExprStatus.DONE
            elif cur.status is ExprStatus.NONE:
                if token == "let":
                    cur.status = ExprStatus.LET
                    vars.append([])
                elif token == "add":
                    cur.status = ExprStatus.ADD
                elif token == "mult":
                    cur.status = ExprStatus.MULT
            elif cur.status is ExprStatus.LET:
                if expression[i] == ")":
                    cur.value = calculateToken(token)
                    cur.status = ExprStatus.LET2
                else:
                    cur.var = token
                    vars[-1].append(token)
                    cur.status = ExprStatus.LET1
            elif cur.status is ExprStatus.LET1:
                scope[cur.var].append(calculateToken(token))
                cur.status = ExprStatus.LET
            elif cur.status is ExprStatus.ADD:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.ADD1
            elif cur.status is ExprStatus.ADD1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.ADD2
            elif cur.status is ExprStatus.MULT:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.MULT1
            elif cur.status is ExprStatus.MULT1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.MULT2
        return cur.value
    
re = Solution().evaluate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))")
print(re)