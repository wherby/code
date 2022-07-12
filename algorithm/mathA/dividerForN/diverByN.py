# https://leetcode.cn/contest/weekly-contest-301/problems/count-the-number-of-ideal-arrays/
# contest\00000c275d69\c301\q4\t4.py
from math import sqrt
def getSub(n):
    ls =[]
    t = int(sqrt(n))
    for i in range(1,t+1):
        if n%i ==0:
            ls.append(i)
            if n //i != i:
                ls.append(n//i)
    return ls

ls = getSub(100)
print(ls)