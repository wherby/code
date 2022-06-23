#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145#problem
#https://codewindow.in/google-codejam-2021-solution/
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



def resolve():
    inp = input()
    ls = inp.split()
    cj,jc =int(ls[0]),int(ls[1])
    str1 = ls[2]
    print(cj,jc,str1,ls)
    cnt =0
    return cnt 

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)