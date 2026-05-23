# https://codeforces.com/gym/106164/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0514/solution/cf106164d.md
# algorithm/codeforce/docs/博弈论SG值/SG值的计算.md
# algorithm/codeforce/docs/FWT/FWT.md



import init_setting
from cflibs import *
from lib.segTreeWithFindFirst2 import *
def main():  
    mod = 998244353
    rev2 = (mod + 1) // 2
    
    def fwt_xor(nums, bit, type):
        for i in range(bit):
            mask = 1 << i
            for j in range(0, 1 << bit, 2 * mask):
                for k in range(mask):
                    x, y = nums[j + k], nums[j + mask + k]
                    nums[j + k] = x + y
                    nums[j + mask + k] = x - y
                    if type == -1:
                        nums[j + k] = nums[j + k] * rev2 % mod
                        nums[j + mask + k] = nums[j + mask + k] * rev2 % mod
    
    n, k, r = MII()
    nums = LII()
    
    sg = [0] * (n + 1)
    seg = SegTree(fmin, n + 1, arr=[-1] * (n + 1))
    
    seg.set(0, 0)
    
    for i in range(1, n + 1):
        sg[i] = seg.max_right(0, lambda x: x >= i - nums[i - 1])
        seg.set(sg[i], i)
    
    ans = 0
    
    cnt = [0] * (1 << 19)
    
    for x in sg:
        cnt[x] += 1
    
    fwt_xor(cnt, 19, 1)
    
    for i in range(1 << 19):
        cnt[i] = pow(cnt[i], r, mod)
    
    fwt_xor(cnt, 19, -1)
    
    ans += cnt[0]
    
    cnt = [0] * (1 << 19)
    
    for i in range(n + 1):
        if i + k > n or sg[i] == sg[i + k]:
            cnt[sg[i]] += 1
    
    fwt_xor(cnt, 19, 1)
    
    for i in range(1 << 19):
        cnt[i] = pow(cnt[i], r, mod)
    
    fwt_xor(cnt, 19, -1)
    
    ans -= cnt[0]
    
    print(ans % mod)

main()