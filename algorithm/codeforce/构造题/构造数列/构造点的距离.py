# https://codeforces.com/problemset/problem/1970/B1
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0819/solution/cf1970b1.md
# 因为距离小于n 而且是偶数，所以曼哈顿距离很容易构建，如果距离不是偶数也可以同理构建


import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    
    print('YES')
    print('\n'.join(f'{i} {i}' for i in range(1, n + 1)))
    print(' '.join(str(i + nums[i] // 2 + 1) if i + nums[i] // 2 < n else str(i - nums[i] // 2 + 1) for i in range(n)))