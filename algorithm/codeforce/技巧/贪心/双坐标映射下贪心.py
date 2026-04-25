# https://codeforces.com/gym/105666/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0415/solution/cf105666b.md
# 同一个元素在两个坐标系上有不一样的值，所以在匹配的时候，匹配点分坐标系匹配，而被匹配的点则记录两个坐标系的对应值
# 采用贪心思维，先选被匹配的一个坐标系的点，用优势匹配坐标系去匹配
# 使用贪心算法，从大到小去匹配，把A坐标系能匹配上的元素都贪心加入备选，然后从备选中选出另一个坐标系映射下最小的值
# 因为是从大到小，在末尾没有被批评的元素，直接用第二哥坐标系最小的值匹配即可
        # while x1:
        #     x1.pop()
        #     heappop(pq)
# stack 里记录的是在另一坐标系的值，就可以与另一坐标系优势的点匹配就可以



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        v1 = []
        v2 = []
        
        for _ in range(n):
            p, s = MII()
            if s == 0:
                v1.append(2 * p)
                v2.append(p)
            else:
                v1.append(p)
                v2.append(2 * p)
        
        x1 = []
        x2 = []
        
        for _ in range(n):
            p, s = MII()
            if s == 0: x1.append(p)
            else: x2.append(p)
        
        x1.sort()
        
        flg = True
        pq = []
        
        for i in sorted(range(n), key=lambda x: -v1[x]):
            while x1 and x1[-1] > v1[i]:
                if len(pq) == 0:
                    flg = False
                    break
                x1.pop()
                heappop(pq)
            heappush(pq, v2[i])
        
        while x1:
            x1.pop()
            heappop(pq)
        
        if not flg: outs.append('NO')
        else:
            x2.sort()
            
            for x in x2:
                if heappop(pq) < x:
                    flg = False
            
            outs.append('YES' if flg else 'NO')
    
    print('\n'.join(outs))