# https://codeforces.com/gym/103476/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0602/solution/cf103476c.md
# 使用欧拉回来覆盖 m*n区域， m%2 == 0 循环相邻的位置是物理相邻的格子


def cover(m,n):
    res = [(0,0),(0,1)]

    for i in range(m):
        for j in range(n-2):
            a,b = res[-1]
            if i%2 ==0:
                res.append((a,b+1))
            else:
                res.append((a,b-1))
        a,b = res[-1]
        if i<m-1:
            res.append((a+1,b))
    a,b = res[-1]
    res.append((a,b-1))
    for i in range(m-2):
        a,b = res[-1]
        res.append((a-1,b))
    return res 

print(cover(4,3))
ans = cover(4,3)

# 广义格雷码的高维扩展
def extends(ans,d):
    ret = []
    m = len(ans)
    for i in range(m):
        s1 = tuple(list([ans[i]]) +[0])
        tmp = [s1]

        for _ in range(d-1):
            t1 = list(tmp[-1])
            t1[-1] = t1[-1] +1 
            t1 = tuple(t1)
            tmp.append(t1)
        if i %2:
            tmp.reverse()
        ret.extend(tmp)
    return ret 

ans2  = extends(ans,5)
print(ans2)

ans3 = extends(ans2,3)
print(ans3)


        