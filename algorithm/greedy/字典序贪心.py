# https://codeforces.com/gym/102890/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0130/solution/cf102890m.md
# 字典序贪心，先计算每个数字出现的位置和前缀和，然后从左到右贪心选取最大的数字，直到每个数字都满足要求为止。
# 用PT记录搜索位置，每次选取一个数字后更新PT到下一个位置。因为贪心做法，找到最大的合法数字后直接跳出循环。然后继续下一个位置的搜索。
# 关键点记录每个点位置上下一个数字出现的位置和前缀和.




import init_setting
from cflibs import *
def main(): 
    s = [int(c) - 1 for c in I()]
    cnt = LII()
    
    n = len(s)
    acc = [[0] * (n + 1) for _ in range(9)]
    next_pos = [[n] * (n + 1) for _ in range(9)]
    
    for i in range(n - 1, -1, -1):
        for j in range(9):
            next_pos[j][i] = next_pos[j][i + 1]
            acc[j][i] = acc[j][i + 1]
        next_pos[s[i]][i] = i
        acc[s[i]][i] += 1
    
    for i in range(n):
        cnt[s[i]] -= 1
    
    for i in range(9):
        cnt[i] = -cnt[i]
    
    ans = []
    total = sum(cnt)
    
    pt = 0
    for _ in range(total):
        for i in range(8, -1, -1):
            npt = next_pos[i][pt]
            flg = True
            
            for j in range(9):
                if acc[j][npt] < cnt[j]:
                    flg = False
            
            if flg and cnt[i]:
                ans.append(i + 1)
                cnt[i] -= 1
                pt = npt + 1
                break
    
    print(''.join(map(str, ans)))