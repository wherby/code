# https://codeforces.com/gym/103059/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0210/solution/cf103059i.md
# 构造拍了是permutation，前缀积余n互不相等，说明每个前缀积都不为0，说明每个数都与前面数的积互质，所以每个数都与n互质，所以n是质数，构造方法就是利用逆元构造出每个数与前面数的积为1的数，这样就保证了前缀积余n互不相等了
# 4是特殊情况？

import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    
    if n == 1:
        print('1')
    elif n == 4:
        print('1 3 2 4')
    else:
        for i in range(2, n):
            if n % i == 0:
                print(-1)
                break
        else:
            ans = [1]
            for i in range(2, n):
                ans.append(i * pow(i - 1, -1, n) % n)
            ans.append(n)
            print(*ans)