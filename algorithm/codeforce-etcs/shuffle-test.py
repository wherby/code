# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0404/solution/cf1530d.md
# https://codeforces.com/problemset/problem/1530/D
from cflibs import *
import random

position= [i for i in range(100000)]
target = [i for i in range(100000)]

k = len(position)
cnt =0
while True:
    cnt +=1
    random.shuffle(position)
    flg = True
    for i in range(k):
        if target[i] == position[i]:
            flg = False
    if flg: break
print(cnt)