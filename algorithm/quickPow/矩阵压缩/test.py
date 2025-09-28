
def quickPow(mat,k):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] =1 
    cur = [list(mat[i]) for i in range(n)]
    while k :
        if k %2 ==1:
            res = multiply(res,cur)
        k = k //2
        cur = multiply(cur,cur)
    return res

def multiply(mata,matb,mod =10**9+7):
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*matb)]
            for row in mata]


def testA(m):
    m1,m2 = [[0]*m for _ in range(m)] ,[[0]*m for _ in range(m)] 
    for i in range(m):
        for j in range(m):
            if i<j:
                m1[i][j]  =1
            if i>j:
                m2[i][j] =1
    m3 = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m-1-i):
            m3[i][j]=1
    mm = quickPow(m3,2)
    mm2 = multiply(m1,m2)
    print(mm,mm2,m3)


testA(5)