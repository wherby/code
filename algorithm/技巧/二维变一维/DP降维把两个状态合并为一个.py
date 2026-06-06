# https://codeforces.com/gym/105437/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0526/solution/cf105437i.md
# DP降维，并且 力量+智力=cur
# 所以 DP[i] 表示 当前状态 i 个力量  cur-i 个智力
# 在多一个点数的时候，需要考虑这个点数加在力量或者智力的时候的转移，如果加在智力的情况，DP值不用变，如果加在力量上，dp[i+1] 可以从dp[i]转移过去
# i其实是一个状态，用差分标记来记录可以得分的状态是多少，因为多一个点数的时候，差分标记的总区域变化，所以需要清楚标记
# 在加一状态转移的时候，fmax(dp[i], dp[i - 1]) 这两个值可以看成两个不同的状态，然后叠加到了现在这个状态，所以需要取最大值，
# 因为随着cur变大，diff形成的得分区域会重叠，所以需要知道变化之前的得分，然后因为cur变大，就算有得分区域重叠，此时状态的得分最多值应该是上一状态两个点的值的最大值




import init_setting
from cflibs import *
def main():
    n, m = MII()
    nums = LII()
    
    cur = 0
    dp = [0]
    diff = [0] * 2
    
    def update():
        global cur
        cur += 1
        
        for i in range(cur):
            diff[i + 1] += diff[i]
        
        for i in range(cur):
            dp[i] += diff[i]
            diff[i] = 0
    
    for x in nums:
        if x == 0:
            update()
            
            dp.append(0)
            diff.append(0)
            
            for i in range(cur, 0, -1):
                dp[i] = fmax(dp[i], dp[i - 1])
        
        elif x > 0:
            if x <= cur:
                diff[x] += 1
                diff[cur + 1] -= 1
        
        else:
            if -x <= cur:
                diff[0] += 1
                diff[cur + x + 1] -= 1
    
    update()
    print(max(dp))