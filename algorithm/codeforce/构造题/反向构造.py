# https://codeforces.com/problemset/problem/1970/D1
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0821/solution/cf1970d1.md
# 因为题目要求的是能根据 q 得到排序，所以排序得到的值是唯一的
# 所以构造的时候直接构造使得不同排列得到的值是唯一即可


import init_setting
from cflibs import *
def main():
    n = II()
    
    calc = [[0] * n for _ in range(n)]
    while True:
        tmp_strs = []
        
        for _ in range(n):
            length = random.randint(10, 30)
            s = ''.join(random.choice('OX') for _ in range(length))
            tmp_strs.append(s)
        
        total_vals = set()
        
        for i in range(n):
            for j in range(n):
                s = tmp_strs[i] + tmp_strs[j]
                k = len(s)
                
                vis = set()
                for x in range(k):
                    for y in range(x, k):
                        vis.add(s[x:y + 1])
                
                calc[i][j] = len(vis)
                total_vals.add(len(vis))
        
        if len(total_vals) == n * n:
            print('\n'.join(tmp_strs), flush=True)
            break
    
    q = II()
    for _ in range(q):
        target = II()
        
        for i in range(n):
            for j in range(n):
                if calc[i][j] == target:
                    print(i + 1, j + 1, flush=True)