


def resolve():
    m,n,k = list(map(lambda x: int(x),input().split()))
    cnt = 0
    g2 = []
    for _ in range(m):
        t1 = input()
        t1=[a for a in t1]
        g2.append(t1)
    g = [["#"]*(n+2) for _ in range(m+2)]
    for i in range(m):
        for j in range(n):
            g[i+1][j+1]= g2[i][j]
    que = []
    for i in range(m+2):
        for j in range(n+2):
            if g[i][j] =="#":
                g[i][j] = k+1
                que.append((i,j,k+1))
            else:
                g[i][j] = 0 

    for a,b,c in que:
        if c ==1: continue
        for x,y in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
            if 0<=x<m+2 and 0<=y<n+2 and g[x][y] ==0:
                g[x][y] = c -1 
                que.append((x,y,c-1))
    for i in range(m+2):
        for j in range(n+2):
            if g[i][j] ==0:
                acc = 0
                q1 = [(i,j)]
                g[i][j] = k+2
                for a,b in q1:
                    acc +=1
                    for x,y in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                        if 0<=x<m+2 and 0<=y<n+2 and g[x][y] ==0:
                            g[x][y] = k+2
                            q1.append((x,y))
                cnt = max(cnt,acc)
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)