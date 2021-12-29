# https://github.com/lydrainbowcat/tedukuri/blob/master/%E9%85%8D%E5%A5%97%E5%85%89%E7%9B%98/%E4%BE%8B%E9%A2%98/0x10%20%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/0x12%20%E9%98%9F%E5%88%97/%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C/CH1201%20%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.cpp
# 用队列模拟了出栈操作，用l和r记录可用值，可以用heapq简化操作，以O（n)的代价
# 队列q 记录了最小值的下标， l 为最优值 q[l:r]是一个单调递增堆栈记录了pre值递增的index， l到r为当index 为i的时候，前m个pre 的递增的序列值
def maxM(arr,m):
    ans = -10**29
    n = len(arr)
    pre=[0]*(1+n)
    for i in range(n):
        pre[i+1] =pre[i] +arr[i]
    l,r =1,1
    q= [0]*(n+1)
    q[1]=0
    for i in range(1,n+1):
        while l<=r and q[l] < i -m : l +=1
        ans = max(ans,pre[i]-pre[q[l]])
        while l <=r and pre[q[r]] >= pre[i]: r -=1  #确保当前的pre值是在递增排序，r-=1就是在做出栈操作。
        r +=1
        q[r] =i
        print(q)
    return ans 





arr= [1,2,-4,5,6,-4,5,1]
re = maxM(arr,4)
print(re)