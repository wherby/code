# https://codeforces.com/gym/105201/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0807/solution/cf105201f.md
# algorithm/string/manachers/manacher.md
# 这个题目解法就是实现了一个Manacher算法。
# 这里和图论结合，表达了一个意思就是，只有在不同的对称点情况下 扩展半径的时候生成的路径连接才是有意义的，单独的Z数组返回值，由于记录的是当前点的半径，这样的连接数量是 n**2 则有大量的重复边
# 这里在Manacher 的新扩展的时候，一定是右端点是新的端点的时候，这样出来的连接一定不会构成环


import init_setting
from cflibs import *
def main():
    s = [ord(c) for c in I()]
    n = len(s)
    
    tmp = []
    for i in range(n):
        if i: tmp.append(-1)
        tmp.append(s[i])
    
    ans = n
    wing = [0] * (2 * n - 1)
    j = 0
    
    for i in range(2 * n - 1):
        if j + wing[j] >= i:
            wing[i] = fmin(j + wing[j] - i, wing[2 * j - i])
        
        while i - wing[i] - 1 >= 0 and i + wing[i] + 1 < 2 * n - 1 and tmp[i - wing[i] - 1] == tmp[i + wing[i] + 1]:
            wing[i] += 1
            if (i - wing[i]) % 2 == 0:
                ans -= 1
        
        if i + wing[i] > j + wing[j]:
            j = i
    
    print(ans)