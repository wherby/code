# https://codeforces.com/gym/105786/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1222/solution/cf105786i.md
# 旋转一个子序列之后使得分段最低
# 一个数字 要通过旋转使得分段减少，如果它的质因数都没出现过，则肯定不能是被选中作为右边的数字 则需要记录它能到达的最前位置，这个位置通过它的质因数查询得到
#        



import init_setting
from cflibs import *
def main(): 
    M = 3 * 10 ** 5
    
    pr = list(range(M + 1))
    
    for i in range(2, M + 1):
        if pr[i] == i:
            for j in range(i, M + 1, i):
                pr[j] = i
    
    def get_prime_factors(x):
        ans = []
        
        while x > 1:
            p = pr[x]
            ans.append(p)
            
            while x % p == 0:
                x //= p
        
        return ans
    
    t = II()
    outs = []
    
    vis = [-1] * (M + 1)
    vis_target = [-1] * (M + 1)
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = 0
        to_delete = 0
        
        for i, x in enumerate(nums):
            tmp = get_prime_factors(x)
            
            flg = True
            pos = i
            for v in tmp:
                if vis[v] != -1:
                    pos = fmin(pos, vis[v])
                    flg = False
                else:
                    vis[v] = i
    
            if flg:
                ans += 1
                for v in tmp:
                    vis_target[v] = i
            else:
                nvis = set()
                
                for v in tmp:
                    if vis_target[v] > pos:
                        nvis.add(vis_target[v])
    
                to_delete = fmax(to_delete, len(nvis))
        
        outs.append(ans - to_delete)
        
        for x in nums:
            tmp = get_prime_factors(x)
            for v in tmp:
                vis[v] = -1
                vis_target[v] = -1
    
    print('\n'.join(map(str, outs)))