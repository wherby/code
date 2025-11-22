
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

def countTo(X,K):
    MSK = (1<<K) -1
    digits =[int(a) for a in str(X)]
    m = len(digits)
    @cache 
    def dp(pos,mask,tight,started):
        nonlocal K,MSK,digits
        if pos == m:
            return 1 if started else 0
        uper = digits[pos] if tight else 9 
        res = 0
        
        for d in range(uper +1):
            new_started = started or (d !=0)
            new_tight = tight and (d == uper)
            if not new_started:
                res += dp(pos+1,mask,new_tight,False)
            new_msk = ((mask<<(d%K)) |(mask >>((K-d)%K))) &MSK
            if new_msk &1:
                continue 
            new_msk = new_msk |1
            res += dp(pos+1,new_msk,new_tight,new_started)
        return res%mod
    res =  dp(0,1,True,False)
    dp.cache_clear()
    return res

from functools import cache
mod =998244353
def resolve():
    L,R,K = list(map(lambda x: int(x),input().split()))
    if len(str(L)) >= K:
        total = (R - L + 1) % mod
        return total
    R1 =min(10**(K-1),R)
    L1 = min(10**(K-1),L)
    
    #print(L,R,K)
    total = (R-L+1)%mod 
    hi = countTo(R1,K)
    lo = countTo(L1-1,K)
    ret = (total - (hi -lo))%mod
    #print(hi,lo,ret,L,R,K,total)
    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)