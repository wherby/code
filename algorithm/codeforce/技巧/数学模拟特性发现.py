# https://codeforces.com/gym/105444/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0615/solution/cf105444k.md
# 这里首先用补位的方式把x,y对齐， 计算了 x+y 的最大的那位进位方式
# 然后这里有一个性质： 把x,y 在进位后的小位保留， 这时 x1+y1 会产生进位，所以有个性质就是把 x1,y1 用+1 或者-1 变成0，或者进位，这时可以发现，+1 一定会比-1更快，因为进位表示了 x1+y1 占领了一大半的空间，
# 所以只考虑+1 的时候，只需要用max(x1,y1)来计算就好了，利用这个性质，可以减少讨论的情况。




import init_setting
from cflibs import *
def main():
    x = [int(c) for c in I()]
    y = [int(c) for c in I()]
    
    x.reverse()
    y.reverse()
    
    while len(x) < len(y): x.append(0)
    while len(y) < len(x): y.append(0)
    
    x.append(0)
    y.append(0)
    
    x.reverse()
    y.reverse()
    
    k = len(x)
    
    total = [0] * k
    chosen = k
    
    for i in range(k - 1, 0, -1):
        if x[i] + y[i] + total[i] >= 10:
            chosen = i
        
        total[i] += x[i] + y[i]
        total[i - 1] += total[i] // 10
        total[i] %= 10
    
    x = x[chosen:]
    y = y[chosen:]
    
    tmp = max(x, y)
    
    k = len(tmp)
    
    ans = []
    
    for i in range(k):
        if i < k - 1: ans.append(9 - tmp[i])
        else: ans.append(10 - tmp[i])
    
    if ans and ans[-1] == 10:
        ans[-1] = 0
        ans[-2] += 1
    
    ans.reverse()
    while ans and ans[-1] == 0:
        ans.pop()
    ans.reverse()
    
    if ans: print(''.join(map(str, ans)))
    else: print(0)