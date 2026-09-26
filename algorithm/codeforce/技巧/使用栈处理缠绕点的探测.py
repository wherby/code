# https://codeforces.com/gym/106642/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0815/solution/cf106642l.md
# 这里题意是保证了最多只移动一根线就可以达到没有缠绕的情况
# 所以就需要找到是否有 xyxy 的缠绕情况，使用栈来处理
# 找到缠绕情况的时候，有可能 xyzxzy 的情况就只能移除x, xyxy的情况就可以移除 x和y ,这样就需要检测是否第2个候选是否可行的，为什么这里最多只有两个候选？
# 因为题意告诉我们只移除一根就能避免缠绕，所以最多只有2个候选，如果有3个则一定不止移除一根


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    special = 0
    vis = [0] * (n + 1)
    stk = []
    
    for x in nums:
        if stk and stk[-1] == x:
            vis[x] = 0
            stk.pop()
        else:
            if vis[x]:
                special = x
                break
            
            vis[x] = 1
            stk.append(x)
    
    if special == 0:
        print(n)
        print(' '.join(map(str, range(1, n + 1))))
    else:
        l = -1
        r = -1
        
        for i in range(2 * n):
            if nums[i] == special:
                if l == -1: l = i
                r = i
        
        vis = [0] * (n + 1)
        
        for i in range(l + 1, r):
            vis[nums[i]] ^= 1
        
        def check(x):
            stk = []
            for v in nums:
                if v != x:
                    if stk and stk[-1] == v:
                        stk.pop()
                    else: stk.append(v)
            return len(stk) == 0
        
        ans = []
        
        if check(special):
            ans.append(special)
        
        v = vis.index(1)
        if check(v): ans.append(v)
        
        ans.sort()
        print(len(ans))
        if ans: print(*ans)