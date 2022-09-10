
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
import sys
input = sys.stdin.readline

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
    n,m,k = tuple(list(map(lambda x: int(x),input().split())))
    ret =0

    return str(ret)
    

def op(caseidx):
    ret= resolve()
    print(ret)
    

for i in range(int(input())):
    op(i)