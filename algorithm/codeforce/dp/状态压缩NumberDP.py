# https://codeforces.com/gym/105940/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1106/solution/cf105940a.md
# 一个子串和能除3 的个数，和前缀和同余个数的组合
# 如果需要所有组合数能除3，则需要判断每个同余的前缀和组合能不能除3 
# （N0,N1,N2) 表示前缀和余数个数， 此时余3个数就是 f= Comb(N0,2) + Comb(N1,2)+ Comb(N2,2) 
# 因为 上面的f是需要mod3,而Comb(N2,2) %3 == Comb(N2%3,2) mod 3 
# 所以可以用状态压缩得到N个字符能存在的状态空间
#  x, y, z = 1, 0, 0  为什么  x=1 , 就和状态计数里需要把 dic[0]=1 作为初始化意义，因为我们需要 Comb(N0,2), 对于0而言，没有值夜是0，所以需要初始化为1 
#


import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    mod = 10 ** 9 + 7
    
    outs = []
    
    def f(i, j, k, cur_mod):
        return ((i * 3 + j) * 3 + k) * 3 + cur_mod
    
    method = [4, 3, 3]
    
    for _ in range(t):
        n = II()
        dp = [0] * 81
        
        for i in range(1, 10):
            x, y, z = 1, 0, 0
            
            if i % 3 == 0: x += 1
            elif i % 3 == 1: y += 1
            else: z += 1
            
            dp[f(x, y, z, i % 3)] += 1
    
        for _ in range(n - 1):
            ndp = [0] * 81
            
            for x in range(3):
                for y in range(3):
                    for z in range(3):
                        for cur_mod in range(3):
                            if dp[f(x, y, z, cur_mod)]:
                                nstatus = [x, y, z]
                                
                                for choice in range(3):
                                    ncur_mod = (cur_mod + choice) % 3
                                    
                                    nstatus[ncur_mod] += 1
                                    nstatus[ncur_mod] %= 3
                                    
                                    nx, ny, nz = nstatus
                                    ndp[f(nx, ny, nz, ncur_mod)] += dp[f(x, y, z, cur_mod)] * method[choice]
                                    ndp[f(nx, ny, nz, ncur_mod)] %= mod
                                    
                                    nstatus[ncur_mod] -= 1
                                    nstatus[ncur_mod] %= 3
            
            dp = ndp
        
        ans = 0
        
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if (x * (x - 1) // 2 + y * (y - 1) // 2 + z * (z - 1) // 2) % 3 == 0:
                        for cur_mod in range(3):
                            ans += dp[f(x, y, z, cur_mod)]
                            ans %= mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))