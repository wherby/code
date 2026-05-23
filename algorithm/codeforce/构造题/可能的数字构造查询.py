# https://codeforces.com/gym/106147/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0303/solution/cf106147b.md
# 用多重 N 进制先筛选可能值，质数底可以确保碰撞数量最小？
# 然后用二分测试candidate碰撞，如果在里面这query的结果是1 
# 对于返回的值也有限制，所以需要在candidate query的时候加入2进制基底作为保底。
# 这里使用了 延迟确认  虽然 l =mid + 1 会丢失 mid 的情况，但是 搜索不到mid的时候， r 最终会变成l-1 又回到mid，这种写法最好不要用。。。
# 这种写法在这个特殊情况是可以这样写，其他情况如果也用了前序数组的话，可能会有问题





import init_setting
from cflibs import *
def main(): 
    def query(vals):
        print('?', len(vals), *vals, flush=True)
        return II()
    
    primes = [2, 3, 5, 7]
    saved_vals = []
    
    for p in primes:
        vals = [1]
        while vals[-1] * p <= 30000:
            vals.append(vals[-1] * p)
        saved_vals.append(query(vals))
    
    candidates = []
    for x in range(1, 30001):
        flg = True
        for i in range(4):
            v = x
            cur = 0
            while v:
                cur += v % primes[i]
                v //= primes[i]
            if cur != saved_vals[i]:
                flg = False
        if flg: candidates.append(x)
    
    l, r = 0, len(candidates) - 1
    while l <= r:
        mid = (l + r) // 2
        
        vals = [1]
        while vals[-1] * 2 <= candidates[mid]:
            vals.append(vals[-1] * 2)
        
        for i in range(mid, r + 1):
            if candidates[i] & -candidates[i] != candidates[i]:
                vals.append(candidates[i])
        
        if query(vals) == 1: l = mid + 1
        else: r = mid - 1
    
    print('!', candidates[r])