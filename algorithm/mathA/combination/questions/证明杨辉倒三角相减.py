# https://leetcode.cn/problems/check-if-digits-are-equal-in-string-after-operations-ii/description/
# 对杨辉倒三角操作求和得到的值是否和化简值相等
from itertools import pairwise
def sumls(ls):
    
    while len(ls)>2:
        tls = []
        for a,b in pairwise(ls):
            tls.append(a+b)
        ls = tls
    return ls

import random

ls = [random.randint(1,2000) for _ in range(1000)]
print(sumls(ls))
import math
def combls(ls):
    ls1,ls2 = ls[:-1],ls[1:]
    def getComb(ls):
        m = len(ls)
        acc =0
        for i,a in enumerate(ls,0):
            acc += math.comb(m-1,i)*a 
        return acc 
    return (getComb(ls1),getComb(ls2))

print(combls(ls))