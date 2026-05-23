# https://codeforces.com/gym/106164/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0513/solution/cf106164c.md
# 1..N 用+-连接，首先1只能是加，所以值域是 2 - v <= n <= v，其次 用需要减去多少个作为判定n， 则（v-n)一定是偶数
# 而1不能被作为减，则 v-2 不能被选中，同理 4-v 也不能，因为和2-v 差了 2//2 这个数不存在
# 为什么 2---X  的差值都存在？ 观察得知如果选一个数字 2.。。i 可以被选中，然后可选多个数字则形成的区间是连续的



import init_setting
from cflibs import *
def main():  
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        
        for i in range(1, 1000):
            v = i * (i + 1) // 2
            
            if 2 - v <= n <= v and (v - n) % 2 == 0 and n != v - 2 and n != 4 - v:
                outs.append(str(i))
                
                chosen = [0] * (i + 1)
                target = (v - n) // 2
                
                for x in range(i, 1, -1):
                    if target >= x and target - x != 1:
                        target -= x
                        chosen[x] = 1
                
                outs.append('1' + ''.join("+-"[chosen[j]] + str(j) for j in range(2, i + 1)))
                break
    
    print('\n'.join(outs))