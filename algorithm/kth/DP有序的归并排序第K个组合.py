# https://codeforces.com/gym/106628/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0730/solution/cf106628f.md
# 因为转移函数是gcd，所以没有单调性，需要遍历前面所有的位置
# 而需要求的是第K大的组合，所以可以在每个位置上保留前K大的组合，并对所有位置使用归并排序


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        cur = [[] for _ in range(n)]
        pts = [0] * n
        
        def msk(x, y): return x * n + y
        
        for i in range(n):
            pq = [msk(-(cur[j][0] + math.gcd(nums[j], nums[i])), j) for j in range(i)]
            heapify(pq)
            
            for _ in range(k):
                if pq:
                    x, y = divmod(heappop(pq), n)
                    cur[i].append(-x)
                    pts[y] += 1
                    
                    if pts[y] < len(cur[y]):
                        heappush(pq, msk(-(cur[y][pts[y]] + math.gcd(nums[y], nums[i])), y))
            
            if len(cur[i]) < k: cur[i].append(0)
            
            for idx in range(i): pts[idx] = 0
        
        total_pq = []
        for x in cur:
            for y in x:
                heappush(total_pq, y)
                if len(total_pq) > k: heappop(total_pq)
        
        if len(total_pq) < k: outs.append(0)
        else: outs.append(total_pq[0])
    
    print('\n'.join(map(str, outs)))