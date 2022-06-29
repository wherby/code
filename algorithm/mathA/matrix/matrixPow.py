def mutliply(m1,m2):
    n = len(m1)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t =0 
            for k in range(n):
                t += m1[i][k]*m2[k][j]
            ret[i][j] = t
    return ret
def matrixPow(mx,y):
    n = len(mx)
    ret =[[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] =1
    cur = mx 
    while y>0:
        if y & 1:
            ret = mutliply(ret,cur)
        cur = mutliply(cur,cur)
        y = y //2
    return ret

a = [[1,0],[1,1]]
print(mutliply(a,a))
print(matrixPow(a,9))
print(a)
b =  [[1,1],[1,1]]
print(matrixPow(b,19))
    