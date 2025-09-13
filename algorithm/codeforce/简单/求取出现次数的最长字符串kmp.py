# https://codeforces.com/gym/101466/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0913/solution/cf101466e.md
# 使用kmp的prep fun 获取子字符串出现的次数

import init_setting
from lib.cflibs import *
from lib.kmp import prefix_function
def main():
    s = I()
    t = I()
    cnt = II()
    
    l, r = 1, len(t)
    
    while l <= r:
        mid = (l + r) // 2
        
        if prefix_function(t[:mid] + '#' + s).count(mid) >= cnt:
            l = mid + 1
        else:
            r = mid - 1
    
    print(t[:r] if r else 'IMPOSSIBLE')

main()