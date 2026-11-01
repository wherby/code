# https://codeforces.com/gym/104603/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1020/solution/cf104603e.md
# 这里如果枚举数量的个数，和a在数列中第几个位置的话，这样数量的起始位置和公差比较难得到整数
# 这里枚举公差的时候，就可以使得树里的个数变成调和级数，然后再带入和与数字是否在数列条件这样枚举的数量是更好验证的



import init_setting
from cflibs import *
def main():
    a, s, l, r = MII()
    
    ans = 0
    
    for diff in range(1, r - l + 1):
        for length in range(1, (r - l) // diff + 1):
            k = length + 1
            if s * 2 % k: continue
            
            v = s * 2 // k - length * diff
            if v % 2 == 0:
                vl = v // 2
                vr = vl + length * diff
                
                if vl >= l and vr <= r and vl <= a <= vr and (a - vl) % diff == 0:
                    ans += 1
    
    if s == a: ans += 1
    
    print(ans)