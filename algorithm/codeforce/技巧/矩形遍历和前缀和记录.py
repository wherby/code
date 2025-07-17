# https://codeforces.com/problemset/problem/253/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0529/solution/cf253d.md
# 这里使用矩形遍历， 在遍历的同时使用tmp记录每个字母所对应的合格前缀和

import init_setting
from cflibs import *
def main():
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    input = lambda: fin.readline().strip()
    print = lambda x: fout.write(str(x))

    n, m, k = MII()
    grid = [[ord(c) - ord('a') for c in I()] for _ in range(n)]

    ans = 0

    for i in range(n):
        cnt = [0] * m
        for j in range(i, n):
            for a in range(m):
                if grid[j][a] == 0:
                    cnt[a] += 1
            
            if j > i:
                l = 0
                cur = 0
                
                tmp = [0] * 26
                
                for r in range(m):
                    cur += cnt[r]
                    
                    while cur > k:
                        if grid[i][l] == grid[j][l]:
                            tmp[grid[i][l]] -= 1
                        cur -= cnt[l]
                        l += 1
                    
                    if grid[i][r] == grid[j][r]:
                        if r > l:
                            ans += tmp[grid[i][r]]
                        tmp[grid[i][r]] += 1

    print(ans)
