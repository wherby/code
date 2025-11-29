# https://codeforces.com/gym/106197/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1126/solution/cf106197l.md



import init_setting

from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        
        ans = [[1] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                ans[i][j] += 2
        
        for i in range(n % 2, n):
            ans[n - 1][i] += 1
        
        for x in ans:
            outs.append(''.join(map(str, x)))
    
    print('\n'.join(outs))

main()