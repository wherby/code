# https://codeforces.com/gym/106531/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0519/solution/cf106531e.md
# 因为是平行或者垂直的斜道，所以最多可以选择一条斜的道路就可以了
# 然后要得到每个斜道使用切入点，这时使用枚举起始分别映射的两个点就可以了，起点直接沿x,y轴到这个斜线的点，终点直接沿x,y轴到斜线的点，枚举这4个点就能确定一定要使用该斜线的最短距离




import init_setting
from lib.cflibs import *
def main():  
    def dis(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    ax, ay, bx, by = MII()
    ans = dis(ax, ay, bx, by)
    
    t = II()
    for _ in range(t):
        b, k = MII()
        
        for x1 in [ax, (ay - b) * k]:
            y1 = k * x1 + b
            for x2 in [bx, (by - b) * k]:
                y2 = k * x2 + b
                
                ans = fmin(ans, dis(ax, ay, x1, y1) + abs(x1 - x2) + dis(x2, y2, bx, by))
    
    print(ans)