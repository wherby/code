# https://codeforces.com/gym/105486/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1110/solution/cf105486i.md
# 如果遍历K 查找是否符合则一定超时，需要从断点位置反推可能的K则可以通过
# 因为断点位置是动态变化的， 可以使用setTree实现



import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import segment_tree
def main(): 
    t = II()
    outs = []
    
    M = 2 * 10 ** 5
    f = [0] * (M + 1)
    for i in range(1, M + 1):
        for j in range(i, M + 1, i):
            f[j] += 1
    
    for _ in range(t):
        n, q = MII()
        nums = LII()
        
        f[0] = n
        
        vals = [0] * n
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                vals[i] = i
        
        seg = segment_tree(vals,math.gcd, 0)
        
        outs.append(f[seg.all_prod()])
        
        for _ in range(q):
            idx, val = MII()
            idx -= 1
            
            nums[idx] = val
            
            if idx:
                vals[idx] = idx if nums[idx] < nums[idx - 1] else 0
                seg.set(idx, vals[idx])
            if idx + 1 < n:
                vals[idx + 1] = idx + 1 if nums[idx + 1] < nums[idx] else 0
                seg.set(idx + 1, vals[idx + 1])
            
            #print(seg.all_prod(),seg.tree)
            outs.append(f[seg.all_prod()])
    
    print('\n'.join(map(str, outs)))

main()