# https://leetcode.cn/problems/solve-the-equation/
class Solution:
    def solveEquation(self, equation: str) -> str:
        factor = val  =0
        i,n,sign =0, len(equation),1 
        while i <n:
            if equation[i] == "=":
                sign = -1
                i +=1 
                continue
            
            s = sign
            if equation[i] == "+":
                i +=1
            elif equation[i] =="-":
                s = -s 
                i +=1
            
            num, valid = 0, False
            while i < n and equation[i].isdigit():
                valid = True
                num = num *10 + int(equation[i])
                i +=1
            
            if i <n and equation[i] =="x":
                factor += s*num if valid else s 
                i +=1
            else:
                val += s*num
        
        if factor ==0:
            return "No solution" if val else "Infinite solutions"
        return f"x={-val //factor}"
                    


re =Solution().solveEquation("x+5-3+x=6+x-2")
print(re)