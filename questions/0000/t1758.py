# https://codeforces.com/contest/1758/problem/D
import math
def generateN(n):
    ls = []
    sm = 0
    mn = 3*n
    for i in range(n-1):
        ls.append(n+i)
        sm += 3*n+i
    start = int(math.sqrt(sm))
    for j in range(start+3*n,7*n):
        t = j - 3*n
        if t*t - sm >= 4*n:
            ls.append(t*t-sm)
            break
    print(len(ls))
    return ls

generateN(200000)