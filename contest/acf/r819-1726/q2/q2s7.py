## Timeout
## Will time out for testing 
## https://codeforces.com/contest/1726/my
############ ---- Input Functions ---- ############
 
    
t= int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n>m:
        print("No")
    else:
        if n %2 ==0 and m%2 ==1:
            print("No") 
        else:
            print("Yes")
            ans=[]
            if n%2==1:
                ans.extend([1]*(n-1)+[m-n+1])
            else:
                ans.extend([1]*(n-2)+[(m-n+2)//2]*2)
            print(*ans,sep=' ')