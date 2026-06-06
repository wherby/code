# https://codeforces.com/gym/103476/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0602/solution/cf103476c.md
# 使用欧拉回来覆盖 m*n区域，  区域面积为奇数，舍去其中一个点

def cover(m,n):
    res = [(0,1)]
    for _ in range(m//2):
        x1,y1 = res[-1]
        res.append((x1+1,y1))
        res.append((x1+1,y1-1))
        res.append((x1+2,y1-1))
        res.append((x1+2,y1))
    x1,y1 = res[-1]
    res.append((x1,y1+1))
    for _ in range(n//2-1):
        x1,y1 = res[-1]
        for j in range(1,m-1):
            res.append((x1-j,y1))
        x1,y1 = res[-1]
        res.append((x1,y1+1))
        for j in range(1,m-1):
            res.append((x1+j,y1+1))
        res.append((x1+m-2,y1+2))
    x1,y1 = res[-1]
    for j in range(1,m):
        res.append((x1-j,y1))
    x1,y1 = res[-1]
    for j in range(1,n-2):
        res.append((x1,y1-j))
    return res 


ans = cover(5,5)
print(ans)
print(len(ans))
# 广义格雷码的高维扩展，因为奇数的时候去除了零点，所以在高维升维的时候需要补回零点
def extends(ans,d):
    ret = []
    m = len(ans)
    for i in range(m):
        s1 = tuple(list(ans[i]) +[0])
        tmp = [s1]

        for idx in range(d-1):
            t1 = list(tmp[-1])
            t1[-1] = t1[-1] +1 
            t1 = tuple(t1)
            tmp.append(t1)
            if i ==0:
                t1 = list(tmp[-1])
                if idx%2 ==0:
                    t1[1] -=1
                    tmp.append(t1)
                else:
                    t1[1] +=1
                    tmp.append(t1)
        if i %2:
            tmp.reverse()
        ret.extend(tmp)
    return ret 

ans2  = extends(ans,5)
print(ans2)
print(len(ans2))



        