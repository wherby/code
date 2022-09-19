
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

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
            #ls = [1 for i in range(n-1)] +[m-n+1]
            a = "1 "*(n-1) + str(m-n+1)
            print(a)
        else:
            ls = [1 for i in range(n-2)] + [(m-n+2)//2 for _ in range(2)]
            print("1 "*(n-1) + str((m-n+2)//2) + " " +str((m-n+2)//2) )
        #ls =[1 for _ in range(10000)]
        #s = " ".join(["1" for a in range(10000)])

    

def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)