# https://codeforces.com/problemset/problem/2195/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0216/solution/cf2195d.md
# 观察找到规律，相邻两项相减等于从当前行号开始的index 和行号之前的index是相反的 prefix ，nums[1]- nums[0]= a1 -(a2+a3+...+an) nums[2]- nums[1]= a1+ a2 -(a3+...+an) 
# total =（a1 +a2 +...+an）=（nums[0]+ nums[n-1]）/（n-1） 之后就可以根据规律求出每一项的值了
# 并且需要维护一个cur来记录当前行之前的index的和，来求出当前行的值，最后一行的值就是total-cur




import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        total = (nums[0] + nums[-1]) // (n - 1)
        
        ans = [0] * n
        cur = 0
        for i in range(n - 1):
            ans[i] = -(nums[i] - nums[i + 1] - total) // 2 - cur
            cur += ans[i]
        
        ans[-1] = total - cur
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(map(str, outs)))

main()