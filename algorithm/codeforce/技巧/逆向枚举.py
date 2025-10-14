# https://codeforces.com/gym/103785/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1011/solution/cf103785h.md
# 寻求构造顺序，逆向枚举任意可能的做法


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    ans = []
    
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            if nums[j] == j + 1:
                ans.append(nums.pop(j))
                break
        else:
            exit(print('NO'))
    
    ans.reverse()
    print('YES')
    print(' '.join(map(str, ans)))