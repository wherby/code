# https://codeforces.com/gym/106682/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0905/solution/cf106682l.md
# 原排列有多少个不同的数字，则一定能贴多少个数字
# 则题意就变成了需要多个个正向或者反向的队列才能满足 LIS = K的递增队列
# 这时我们已知下一个数字是多少和当前位置，所以可以用二分的方式找到下一个目标数字的位置，正反查找得到贪心最长序列


import init_setting
from cflibs import *
def main():
    n, m = MII()
    nums = LII()
    
    pos = [[] for _ in range(m + 1)]
    for i in range(n):
        pos[nums[i]].append(i)
    
    target = [i for i in range(m + 1) if pos[i]]
    
    k = len(target)
    start = 0
    ans = 0
    
    while start < k:
        nstart1 = 0
        cur1 = 0
        for j in range(start, k):
            p = bisect.bisect_left(pos[target[j]], cur1)
            if p == len(pos[target[j]]): break
            nstart1 = j
            cur1 = pos[target[j]][p]
        
        nstart2 = 0
        cur2 = n
        for j in range(start, k):
            p = bisect.bisect_left(pos[target[j]], cur2) - 1
            if p == -1: break
            nstart2 = j
            cur2 = pos[target[j]][p]
        
        start = fmax(nstart1, nstart2) + 1
        ans += 1
    
    print(k, ans)