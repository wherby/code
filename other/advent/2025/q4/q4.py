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
    lss =[]
    for line in ls:
        tmp = [0 if a =="." else 1 for a in line]
        lss.append(tmp )
    m,n = len(lss),len(lss[0])
    def getSum(x,y):
        sm = 0 
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 0<=i< m and 0<=j<n:
                    sm += lss[i][j]
        return sm - lss[x][y]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if getSum(i,j) <4 and lss[i][j] ==1:
                cnt +=1
                #print(i,j)
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
    