# https://codeforces.com/problemset/problem/220/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0723/solution/cf220c.md
# 当x往左移动的循环队列
# x,y在不同的相对位置的时候，有两种情况；有两个队列，1队列保存减少的值，2队列保存增加的值
# 当x大于y: 先距离减少[0初始值的时候是v]，  再距离增大，到达0之后又会跳到n-1的位置，然后有距离减少
#        减少->增加   减少到0 的时候，就从减少队列去掉，然后放增加队列
#        到达0以后的时候，因为一定在增加队列，所以在增加队列去除0的影响，在增加队列加入n-1的影响
# 当x小于y : 距离先增大，然后到0，跳转到n-1，换队列变成减少队列,然后减少到0，然后增加距离

import init_setting
from cflibs import *

def main():
    n = II()
    p1 = LGMI()
    p2 = LGMI()

    inf = 2 * n
    
    v1 = [inf]
    v2 = [inf]
    updates1_add = [[] for _ in range(n+1)]
    updates1_remove = [[] for _ in range(n+1)]
    updates2_add = [[] for _ in range(n+1)]
    updates2_remove = [[] for _ in range(n+1)]
    pos1 = [0]*n 
    pos2 = [0]*n 
    for i in range(n):
        pos1[p1[i]] = i 
        pos2[p2[i]] = i 

    for i in range(n):
        x= pos2[i]
        y= pos1[i]
        v = abs(x-y)
        if x >=y:
            updates1_add[0].append(v)
            updates1_remove[v].append(v)
            updates2_add[v].append(-v)
            updates2_remove[x+1].append(-v)
            updates1_add[x+1].append((x+1) + (n-1-y))
        else:
            updates2_add[0].append(v)
            updates2_remove[x+1].append(v)
            updates1_add[x+1].append((x+1) + (n-1-y))
            updates1_remove[(x+1)+(n-1-y)].append((x+1)+ (n-1-y))
            updates2_add[(x+1) + (n-1-y)].append(-((x+1)+(n-1-y)))
    

    vis1 = [0] * (3 * n + 5)
    vis2 = [0] * (3 * n + 5)
    
    ans = [0] * n
    
    for i in range(n):
        for x in updates1_add[i]:
            heappush(v1, x)
        
        for x in updates1_remove[i]:
            vis1[x] += 1
        
        while v1[0] < inf and vis1[v1[0]]:
            vis1[v1[0]] -= 1
            heappop(v1)
        
        for x in updates2_add[i]:
            heappush(v2, x)
        
        for x in updates2_remove[i]:
            vis2[x] += 1
        
        while v2[0] < inf and vis2[v2[0]]:
            vis2[v2[0]] -= 1
            heappop(v2)
        
        ans[i] = fmin(v1[0] - i, v2[0] + i)
    
    print(*ans, sep='\n')

main()