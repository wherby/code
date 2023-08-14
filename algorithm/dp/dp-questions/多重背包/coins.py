# page 307 
# github\tedukuri\配套光盘\例题\0x50 动态规划\0x52 背包\Coins

def coins(m,a,c):
    f = [0]*(m+1)
    f[0] = 1
    n = len(a)
    for i in range(n):
        used = [0]*(m+1)
        for j in range(a[i],m+1):
            if not f[j] and f[j-a[i]] and used[j-a[i]] < c[i]:
                f[j] =1
                used[j] = used[j-a[i]] +1
        #print(used)
    ans = 0 
    for i in range(1,m+1):
        if f[i]:
            ans +=1
            #print(i)
    #print(f)
    return ans 

re = coins(100,[2,5],[10,10])
print(re) 