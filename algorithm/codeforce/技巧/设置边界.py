# https://codeforces.com/problemset/problem/747/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0529/solution/cf747e.md
# 如果用stack记录每个节点的子节点数目剩余，为0的时候就pop，在根节点的时候，根节点没办法pop，则把根节点设置大值则可以变成一致性操作

import init_setting
from cflibs import *
def main():
    s = I().split(',')
    n = len(s)

    ans = []

    cur = [10 ** 7]

    for i in range(0, n, 2):
        x = s[i]
        v = int(s[i + 1])
        
        while cur[-1] == 0:
            cur.pop()
        
        if len(cur) - 1 == len(ans):
            ans.append([])
        ans[len(cur) - 1].append(x)
        
        cur[-1] -= 1
        
        cur.append(v)

    print(len(ans))
    print('\n'.join(' '.join(x) for x in ans))