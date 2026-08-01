# https://codeforces.com/gym/106628/problem/O
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0727/solution/cf106628o.md
# 使用相对排名构建，可以正序完成，否则需要逆序计算并使用线段树或者有序数组



import init_setting
from lib.cflibs import *
def main():
    def query(idxs):
        print('?', len(idxs), *idxs, flush=True)
        return II()
    
    def answer(p):
        print('!', *p, flush=True)
    
    t = II()
    
    for _ in range(t):
        n = II()
        cur = 0
        
        ans = [0] * n
        ans[0] = 1
        
        for i in range(2, n + 1):
            ncur = query(list(range(1, i + 1)))
            val = i - (ncur - cur)
            
            for j in range(i):
                if ans[j] >= val:
                    ans[j] += 1
            ans[i - 1] = val
            
            cur = ncur
    
        answer(ans)