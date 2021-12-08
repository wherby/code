# https://github.com/wisdompeak/LeetCode/blob/master/Template/Combination-Number/comb.cpp

comb = [[0]*1001 for i in range(1001)]
for i in range(1001):
    comb[i][i] , comb[i][0]=1,1
    if i == 0: continue
    for j in range(1,i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

print(comb[100][:10])

def comb2(n,m):
    cnt = 1
    for i in range(m):
        cnt *=n-i
        cnt //= i+1
    return cnt

print(comb2(100,2))


# combination number
#>>> from math import comb
#>>> comb(10,3)
#120