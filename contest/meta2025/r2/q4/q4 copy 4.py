

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/dividing_passcodes_validation_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=False

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f


from functools import cache
mod =998244353
def resolve():
    L,R,K = list(map(lambda x: int(x),input().split()))
    R =min(10**(K-1),R)
    L = min(10**(K-1),L)
    @cache 
    def dp(pos,mask,tight,digits,started):
        if pos == len(digits):
            return 1 
        uper = int(digits[pos]) if tight else 9 
        res = 0
        if not started: 
            res =dp(pos+1,mask,False,digits,False)
        for d in range(uper +1):
            new_started = started or (d !=0)
            new_tight = tight and (d == uper)
            
            if mask &(1<<d):
                continue 
            new_msk = mask |(1<<d)
            new_msk = new_msk//(1<<(d)) + ((new_msk%(1<<d)) << ((K-d)%K))
            res += dp(pos+1,new_msk,new_tight,digits,new_started)
        return res%mod
    #print(L,R,K)
    total = (R-L+1)%mod 
    hi = dp(0,1,True,str(R),False)
    lo = dp(0,1,True,str(L-1),False)
    ret = (total - (hi -lo))%mod

    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)