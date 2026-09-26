# https://leetcode.cn/contest/weekly-contest-514/ranking/?region=local_v2
# thunderfire

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n=len(nums)
        z=1
        while z<n:
            z<<=1
        e=(-1,-1,0)
        t=[e]*(z<<1)

        def f(a,b):
            if a[0]<0:
                return b
            if b[0]<0:
                return a
            return (a[0],b[1],a[2]+b[2]+b[0]*(b[0]-a[1]))

        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                t[z+i]=(i,i,0)
        for i in range(z-1,0,-1):
            t[i]=f(t[i<<1],t[i<<1|1])

        def u(i):
            p=z+i
            v=(i,i,0) if 0<i<n-1 and nums[i]>nums[i-1] and nums[i]>nums[i+1] else e
            if t[p]==v:
                return
            t[p]=v
            p>>=1
            while p:
                t[p]=f(t[p<<1],t[p<<1|1])
                p>>=1

        r=[]
        for q in queries:
            if q[0]==1:
                l,h=q[1],q[2]
                x=l+1+z
                y=h+z
                a=b=e
                while x<y:
                    if x&1:
                        a=f(a,t[x])
                        x+=1
                    if y&1:
                        y-=1
                        b=f(t[y],b)
                    x>>=1
                    y>>=1
                a=f(a,b)
                r.append(0 if a[0]<0 else h*(a[1]-l)-a[0]*(a[0]-l)-a[2])
            else:
                i,v=q[1],q[2]
                nums[i]=v
                for j in range(max(1,i-1),min(n-1,i+2)):
                    u(j)
        return r