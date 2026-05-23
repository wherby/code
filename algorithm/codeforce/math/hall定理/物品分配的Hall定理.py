# https://codeforces.com/gym/106527/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0520/solution/cf106527c.md
# algorithm/codeforce/docs/hall定理.md 
# 已知所有题目的回答情况，求大于自己分数的最少人数的人数数量
# 这里采用了空位视角，空位数量《超过自己的人产生的数量 + 等于自己的人产生空位的数量
# 假设等于自己的人的空位为v个人，则超过自己的人的数量为n-v
# algorithm/codeforce/math/hall定理/物品分配的Hall定理 copy.py 这里的解答更容易理解。。。






import init_setting
from cflibs import *
def main():  
    t = II()
    outs = []
    
    for _ in range(t):
        n, p, x = MII()
        nums = LII()
        
        x = p - x
        
        cnt = [0] * (n + 1)
        for v in nums:
            cnt[n - v] += 1
        
        nums.clear()
        
        for i in range(n + 1):
            for _ in range(cnt[i]):
                nums.append(i)
        
        cur = 0
        ans = n
        
        for i in range(p):
            cur += nums[i]
            if x - (p - i - 1) > 0:
                ans = fmin(ans, cur // (x - (p - i - 1)))
        
        outs.append(n - ans)
    
    print('\n'.join(map(str, outs)))

main()