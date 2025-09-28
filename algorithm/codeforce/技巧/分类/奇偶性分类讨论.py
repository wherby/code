# https://codeforces.com/gym/106032/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0927/solution/cf106032j.md
# 数字个奇偶性的合并规律
# 对于奇数，最近的奇数就是0，也表示不会移动，和题意一致
# 因为mod M 是一个环，计算右边最远的奇数的时候，先正常从右到左遍历，然后合并0和M的值，再遍历一次。


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    inf = 10 ** 9
    
    for _ in range(t):
        n, m, q = MII()
        nums = LII()
        cnt = [0] * (m + 1)
        
        for x in nums:
            cnt[x] ^= 1
        
        next_odd = [inf] * (m + 1)
        
        for i in range(m + 1):
            if cnt[i]:
                next_odd[i] = 0
        
        for i in range(m, 0, -1):
            next_odd[i - 1] = fmin(next_odd[i - 1], next_odd[i] + 1)
        
        next_odd[m] = fmin(next_odd[m], next_odd[0])
        for i in range(m, 0, -1):
            next_odd[i - 1] = fmin(next_odd[i - 1], next_odd[i] + 1)
        
        cnt = 0
        for _ in range(q):
            query = LII()
            if query[0] == 1: cnt += 1
            else:
                x = nums[query[1] - 1]
                step = fmin(cnt, next_odd[x])
                outs.append((x + step - 1) % m + 1)
    
    print('\n'.join(map(str, outs)))

main()