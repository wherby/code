import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

ls = []
try:
    with open(filename, 'r') as file:
        for line in file:
            ls.append(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")



def solve():
    cur =50
    cnt =0
    for line in ls:
        lst = cur
        num = int(line[1:])
        cnt += num//100
        num = num%100
        if line[0] == "L":
            cur -= num
        else:
            cur += num
        if (cur <0  and lst != 0) or cur >100:
            cnt +=1
        cur = cur%100 
        if cur ==0:
            cnt +=1
       #  print(line, cnt,cur)
    print(cnt)

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    