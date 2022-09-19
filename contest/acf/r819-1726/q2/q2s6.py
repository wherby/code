## Will time out for testing 
## https://codeforces.com/contest/1726/my
############ ---- Input Functions ---- ############
def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return list((map(int,input().split())))

    

for i in range(int(input())):
    n,m = tuple(list(map(lambda x: int(x),input().split())))
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