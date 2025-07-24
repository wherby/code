# https://codeforces.com/problemset/problem/847/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0724/solution/cf847f.md
# 暴力分类枚举不同的情况
# 把idx =0 作为null 标记，在选择其他节点的时候，如果都比当前节点大，则加在0 节点

import init_setting
from cflibs import *
def main():
    n, k, m, a = MII()
    nums = LII()

    ans = [2] * (n + 1)

    for i in range(1, n + 1):
        # 考虑最有利的情况
        
        cnt = [0] * (n + 1)
        last_vote = [-1] * (n + 1)
        
        for j in range(a):
            cnt[nums[j]] += 1
            last_vote[nums[j]] = j
        
        for j in range(a, m):
            cnt[i] += 1
            last_vote[i] = j
        
        if cnt[i] == 0:
            ans[i] = 3
            continue
        
        else:
            total = 1
            for j in range(1, n + 1):
                if cnt[j] > cnt[i] or (cnt[j] == cnt[i] and last_vote[j] < last_vote[i]):
                    total += 1
            if total > k:
                ans[i] = 3
                continue
        
        # 考虑最不利的情况
        
        cnt = [0] * (n + 1)
        last_vote = [-1] * (n + 1)
        
        for j in range(a):
            cnt[nums[j]] += 1
            last_vote[nums[j]] = j
        
        for tmstamp in range(a, m):
            
            # 选择紧随其后的对手
            cur_cnt, idx = -1, 0
            for j in range(1, n + 1):
                if cnt[j] < cnt[i] or (cnt[j] == cnt[i] and last_vote[j] > last_vote[i]):
                    if cnt[j] > cur_cnt:
                        cur_cnt = cnt[j]
                        idx = j
            
            cnt[idx] += 1
            last_vote[idx] = tmstamp

        if cnt[i]:
            total = 1
            for j in range(1, n + 1):
                if cnt[j] > cnt[i] or (cnt[j] == cnt[i] and last_vote[j] < last_vote[i]):
                    total += 1
            if total <= k:
                ans[i] = 1

    print(' '.join(map(str, ans[1:])))