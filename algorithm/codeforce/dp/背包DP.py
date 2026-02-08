# https://codeforces.com/gym/105327/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0203/solution/cf105327k.md
# 将数组分成两个和相等的子集，然后交替输出两个子集的元素
# 背包dp 记录每个和对应的最后一个元素下标，然后倒推得到子集
# 因为index从0开始，所以dp数组初始化为-2，表示不可达 用-1表示和为0时不需要元素
# 按照题意 注意输出顺序时，贪心地从和较小的子集取元素，保证交替输出
# DP记录index的时候可能有覆盖，and dp[j] == -2 这个条件很重要，防止覆盖




import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    total = sum(nums)
    
    if total % 2:
        print(-1)
    else:
        M = total // 2
    
        dp = [-2] * (M + 1)
        dp[0] = -1
        
        for i in range(n):
            x = nums[i]
            
            for j in range(M, x - 1, -1):
                if dp[j - x] != -2 and dp[j] == -2:
                    dp[j] = i
        
        if dp[M] == -2:
            print(-1)
        else:
            vis = [0] * n
            cur = M
            
            while cur:
                vis[dp[cur]] = 1
                cur -= nums[dp[cur]]
            
            v1 = [nums[i] for i in range(n) if vis[i]]
            v2 = [nums[i] for i in range(n) if not vis[i]]
            
            s1 = s2 = 0
            pt1 = pt2 = 0
            
            ans = []
            
            while pt1 < len(v1) or pt2 < len(v2):
                if s1 <= s2:
                    s1 += v1[pt1]
                    ans.append(v1[pt1])
                    pt1 += 1
                else:
                    s2 += v2[pt2]
                    ans.append(v2[pt2])
                    pt2 += 1
            
            print(*ans)