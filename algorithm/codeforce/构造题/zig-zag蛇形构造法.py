# https://codeforces.com/gym/105401/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0606/solution/cf105401d.md
# 蛇形构造法，使得连续的位置的差为奇数，则上下边的连接为差的和为偶数，然后用最大最小的奇数差往中间靠拢，则两奇数的差正好为偶数部分




import init_setting
from cflibs import *
def main():
    n = II()
    
    ans = [1]
    
    l = 1
    r = 2 * n + 1
    
    for i in range(n + 1):
        if i % 2 == 0:
            ans.append(ans[-1] + r)
            r -= 2
        else:
            ans.append(ans[-1] - l)
            l += 2
    
    print(' '.join(map(str, ans)))

    for a,b in pairwise(ans):
        print(abs(a-b))
    n = len(ans)
    for i in range(n-2):
        print(abs(ans[i] - ans[i+2]))
main()