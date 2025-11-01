# https://codeforces.com/gym/105613/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1027/solution/cf105613e.md
# 所有pair 总数为 n*(n-1)//2
# 所有小于它的数字都可以表示为 i*(i-1)//2 + j  (j<=i)
# 所以把前 i个数字都放置成3，然后把其中j个数字变成6，则 i*(i-1)//2个pair性质不变，再加上2用来调和j个pair
# 然后在后面加上很大的奇数不能被3整除的数字就可以保证没有两两不整除，因为奇数减少的时候，也不会到1/3位置，所以之间也不会有整除关系




import init_setting
from cflibs import *
def main(): 
    n = II()
    k = II()
    
    if n * (n - 1) // 2 < k: exit(print(-1))
    
    for i in range(1, n + 1):
        if i * (i + 1) // 2 > k:
            ans = [3] * i
            k -= i * (i - 1) // 2
            for i in range(k):
                ans[i] = 6
            if k: ans.append(2)
            break
    
    for i in range(999997, 0, -6):
        if len(ans) < n: ans.append(i)
        if len(ans) < n: ans.append(i - 2)
    
    print(' '.join(map(str, ans)))