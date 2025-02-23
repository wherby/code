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

n = 0
ans = 0

def search(idx,s):
    global ans
    st =[]
    tmp = ""
    a=idx
    while idx<n:
        if s[idx]==",":
            if len(tmp)>0 and len(st) ==0:
                st.append(int(tmp))
                tmp =""
            else:
                return idx
        elif s[idx] == ")":
            if len(tmp)>0 and len(st)==1:
                ans += int(tmp) *int(st[0])
                print(s[a-4:idx+1],a,ans)
                return idx
            else:
                #print(s[a-4:idx+1],a)
                return idx
        elif s[idx].isdigit():
            tmp += s[idx]
        else:
            #print(s[a-4:idx+1],a,"aaa")
            return idx
        idx +=1
    


def solve():
    global n
    ls =""
    for _ in range(6):
        t = input()
        ls+=t
    #print(ls)
    n = len(ls)
    cur = 0
    cnt =0
    while cur <n:
        if cur >=3 and ls[cur-3:cur+1] == "mul(":
            #print(cur)
            cnt +=1
            print(ls[cur-3:cur+10])
            cur = search(cur+1,ls)
            #cur +=1
            #print(cur,ans)
        else:
            cur +=1
    print(cnt)
    return ans

    


solve()
print(ans)