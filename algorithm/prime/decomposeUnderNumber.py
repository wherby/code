# https://leetcode.com/contest/weekly-contest-471/problems/longest-balanced-substring-ii/description/

from collections import defaultdict,deque
from collections import Counter
def getDecompositListUnderN(n):
    dic =[Counter() for _ in range(n+2)]
    visited=[False for _ in range(n+2)]
    dic[1][1] =1 ## ??是否需要1
    for i in range(2,n+1):
        if visited[i]:
            continue
        dic[i][i] =0 ###??
        for j in range(i,n+1,i):
            t= j
            visited[j] =1
            while t%i ==0:
                dic[j][i] +=1
                t = t//i
    return dic


d = getDecompositListUnderN(100000)
print(d[100])