# https://codeforces.com/gym/106495/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0425/solution/cf106495h.md
# algorithm/string/docs/manacher算法的使用.md
# 需要A与B 做 字符串匹配，则用编码把 A,B字符串对应位置编码在一起，就变成了简单的字符串匹配
# 需要计算的是首位字符串匹配和中间一段相连的对称字符串的数量
# 对于中间对称字符串的数量，使用manacher计算最大匹配，然后用差分标记


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        s1 = [ord(c) % 26 for c in I()]
        s2 = [ord(c) % 26 for c in I()]
        
        n = len(s1)
        s = [0] * n
        
        for i in range(n):
            s[i] = s1[i] * 26 + s2[i]
        
        tmp = [s[i // 2] if i % 2 == 0 else -1 for i in range(2 * n - 1)]
    
        manacher = [0] * (2 * n - 1)
        starting = [0] * (2 * n)
        ending = [0] * (2 * n)
        
        j = 0
        for i in range(2 * n - 1):
            if j + manacher[j] >= i:
                manacher[i] = fmin(manacher[2 * j - i], j + manacher[j] - i)
            while i - manacher[i] - 1 >= 0 and i + manacher[i] + 1 < 2 * n - 1 and tmp[i - manacher[i] - 1] == tmp[i + manacher[i] + 1]:
                manacher[i] += 1
            if i + manacher[i] > j + manacher[j]:
                j = i
            
            starting[i - manacher[i]] += 1
            starting[i + 1] -= 1
            
            ending[i] += 1
            ending[i + manacher[i] + 1] -= 1
    
        for i in range(1, 2 * n):
            starting[i] += starting[i - 1]
            ending[i] += ending[i - 1]
        
        ans = 0
        for i in range(n):
            if s1[i] != s2[n - 1 - i] or s2[i] != s1[n - 1 - i]:
                break
            ans += 1
            if i < n - 1:  # 没有判断的话会数组越界
                ans += starting[2 * (i + 1)]
                ans += ending[2 * (n - i - 2)]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))