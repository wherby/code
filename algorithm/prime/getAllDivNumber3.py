# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0819/solution/cf104544a.md
import math 
def getAllDiv(N):
    res  =[]
    for i in range(1,int(math.sqrt(N))+2):
        if i*i >N :break
        if N%i ==0:
            res.append(i)
            if N//i != i:
                res.append(N//i)
    res.sort()
    return res

print(getAllDiv(1080*(2**10)*(3**10)))