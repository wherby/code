
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
MOD =998244353
MOD = 998244353

def count_k_weak(L, R, K):

    def count_non_weak(limit):
        if limit < 0:
            return 0
            
        digits = list(map(int, str(limit)))
        n = len(digits)
        
        if n >= K:
            return count_fixed_length_up_to(K - 1)
        
        
        @cache
        def dp(pos, sum_mod, mask, tight, started):
            if pos == n:
                return 1 if started else 0
                
            res = 0
            upper = digits[pos] if tight else 9
            
            for dig in range(upper + 1):
                new_tight = tight and (dig == upper)
                
                if not started:
                    if dig == 0:
                        res += dp(pos + 1, 0, mask, new_tight, False)
                    else:
                        new_mask = 1 | (1 << dig)
                        res += dp(pos + 1, dig, new_mask, new_tight, True)
                else:
                    new_sum = (sum_mod + dig) % K
                    if mask & (1 << new_sum):
                        continue
                    new_mask = mask | (1 << new_sum)
                    res += dp(pos + 1, new_sum, new_mask, new_tight, True)
            
            return res % MOD
        
        return dp(0, 0, 1, True, False)
    
    def count_fixed_length_up_to(max_len):
        total = 0
        for length in range(1, min(max_len + 1, K)):
            total = (total + count_fixed_length(length)) % MOD
        return total
    
    def count_fixed_length(length):
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dfs(pos, sum_mod, mask):
            if pos == length:
                return 1
                
            res = 0
            start_digit = 1 if pos == 0 else 0
            
            for dig in range(start_digit, 10):
                new_sum = (sum_mod + dig) % K
                if mask & (1 << new_sum):
                    continue
                res += dfs(pos + 1, new_sum, mask | (1 << new_sum))
            
            return res % MOD
        
        return dfs(0, 0, 1)
    
    total = (R - L + 1) % MOD
    non_weak = (count_non_weak(R) - count_non_weak(L - 1)) % MOD
    return (total - non_weak) % MOD

def resolve():
    L,R,K = list(map(lambda x: int(x),input().split()))
    R =min(10**K,R)
    L = min(10**K,L)

    return count_k_weak(L,R,K)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)