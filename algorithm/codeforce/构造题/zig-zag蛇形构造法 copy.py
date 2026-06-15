# https://codeforces.com/gym/105401/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0606/solution/cf105401d.md
# 蛇形构造法，使得连续的位置的差为奇数，则上下边的连接为差的和为偶数，然后用最大最小的奇数差往中间靠拢，则




import init_setting
from cflibs import *
import sys


def main():
    n = II()
    
    # 1. 构造完美的中间链差值序列 (d_1, d_2, ..., d_{n+1})
    # 我们希望这些奇数交错，使得相邻项之和恰好唯一覆盖 2 到 2n 的偶数
    diffs = []
    l = 1
    r = 2 * n + 1
    
    # 用左右指针交替取出 [1, 3, 5, ..., 2n+1]
    for i in range(n + 1):
        if i % 2 == 0:
            diffs.append(r)
            r -= 2
        else:
            diffs.append(l)
            l += 2
            
    # 2. 通过差值序列恢复顶点权值（交错加减）
    ans = [0] * (n + 2)
    ans[0] = 0
    for i in range(n + 1):
        if i % 2 == 0:
            ans[i + 1] = ans[i] + diffs[i]
        else:
            ans[i + 1] = ans[i] - diffs[i]
            
    # 3. 整体平移，消除 0 和负数（提示 5）
    min_val = min(ans)
    if min_val <= 0:
        shift = 1 - min_val
        ans = [x + shift for x in ans]
        
    # 4. 打印结果
    print(' '.join(map(str, ans)))
    for a,b in pairwise(ans):
        print(abs(a-b))
    n = len(ans)
    for i in range(n-2):
        print(abs(ans[i] - ans[i+2]))

if __name__ == '__main__':
    main()