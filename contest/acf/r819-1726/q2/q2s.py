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

def resolve():
    n,m = tuple(list(map(lambda x: int(x),input().split())))
    if n>m:
        print("No")
        return 
    else:
        if n %2 ==0 and m%2 ==1:
            print("No")
            return 
        print("Yes")
        if n%2 ==1:
            ls = [1 for i in range(n-1)] +[m-n+1]
        else:
            ls = [1 for i in range(n-2)] + [(m-n+2)//2 for _ in range(2)]
        s = " ".join([str(a) for a in ls])
        print(s)
        #ls =[1 for _ in range(10000)]
        #s = " ".join(["1" for a in range(10000)])

    

def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)