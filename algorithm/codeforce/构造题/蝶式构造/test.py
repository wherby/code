import itertools
import random
N = 10
ls = [i for i in range(1,N+1)]
lss = list(itertools.permutations(ls))
nd = random.randint(100,1399)
ls = lss[nd]
print(ls)

def query(idlist):
    global ls
    tmp = []
    for idx in idlist:
        tmp.append(ls[idx-1])
    tmp.sort()
    return tmp

def recover():
    n = N
    pos = [0] * (n + 1)
    
    for i in range(10):
        tmp = []
        for j in range(1, n + 1):
            if j >> i & 1:
                tmp.append(j)
        
        if len(tmp):
            nums = query(tmp)
            for v in nums:
                pos[v] |= 1 << i
    
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[pos[i]] = i
    
    print('!', *ans[1:])

recover()