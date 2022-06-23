def rowPrefix(g):
    m,n = len(g),len(g[0])
    reg = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            reg[i][j] = reg[i][j-1] + g[i][j]
    return reg

def colPrefix(g):
    m,n = len(g),len(g[0])
    reg = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            reg[i][j] = reg[i-1][j] + g[i][j]
    return reg

# Verified in https://leetcode-cn.com/contest/weekly-contest-289/problems/maximum-trailing-zeros-in-a-cornered-path/

def oneDPrefix(g,fn, direction=0,defaultV=(0,0)):
    m,n = len(g),len(g[0])
    reg = [[defaultV]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if direction ==0:
                reg[i][j] = fn(reg[i][j-1] ,g[i][j])
            else:
                reg[i][j] = fn(reg[i-1][j] , g[i][j])
    return reg