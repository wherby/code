# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E?source=facebook
# sub question
# 已知 有 n 个数字，求可以给数字ai 减少任意数的情况下，可能使得数字能组成1，2，，m的最大m值是多少的排列

import random
from collections import Counter
ls = [random.randint(1,10000)  for _ in range(10000)]

def getMaxCount(ls):
    c = Counter(ls)
    ret  = acc= len(ls)
    idx = 1
    while idx <=ret:  # 用ret的最小值动态控制循环次数
        acc -= c[idx]
        ret = min(ret, acc + idx )
        idx +=1
    return ret 

print(getMaxCount(ls))

ls2 = [1,1,3,4,4,4,5,7]
print(getMaxCount(ls2))