# https://codeforces.com/gym/105706/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0617/solution/cf105706a.md
# 求当前位置的下一个位置用逆序方式就可以求得
# 因为求L,R 范围内的最大的长度是从1开始，所以需要记录每个位置开始后的真正起点就是下一个1的位置
# 所以dp[i][j] 是记录 在j的位置走了i步之后的位置，这里不用数字大小作为DP变量，因为j的位置本身就有大小信息，
# 在dp上递推的时候把位置信息与数字大小“压缩"在一起了,位置信息的信息量比数字大小大，因为数字大小有重复的，所以不能用做DP递推

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        nums = LII()
        
        next_pos1 = [n] * n
        next_pos = [[n] * (n + 1) for _ in range(20)]
        
        pos = [n] * (n + 2)
        
        for i in range(n - 1, -1, -1):
            next_pos[0][i] = pos[nums[i] + 1]
            pos[nums[i]] = i
            next_pos1[i] = pos[1]
        
        for i in range(19):
            for j in range(n):
                next_pos[i + 1][j] = next_pos[i][next_pos[i][j]]
    
        ans = []
        for _ in range(q):
            l, r = GMI()
            
            if next_pos1[l] > r: ans.append(1)
            else:
                l = next_pos1[l]
                res = 2
                
                for i in range(19, -1, -1):
                    if next_pos[i][l] <= r:
                        l = next_pos[i][l]
                        res += 1 << i
                
                ans.append(res)
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))