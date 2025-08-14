# Permutation

# a = [1,1,1,2]
# >>> a = [1,1,1,2]
# >>> ls = list(permutations(a))
# >>> print(ls)
# [(1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (1, 2, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (1, 2, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (1, 2, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1)]
from collections import Counter

def permutate(ls):
    c = Counter(ls)
    keys = list(c.keys())
    ret = []
    n = len(ls)
    def bfs(used,tmp):
        if used == n:
            ret.append(list(tmp))
            return 
        for k in keys:
            if c[k]>0:
                c[k]-=1
                tmp.append(k)
                bfs(used+1,tmp)
                tmp.pop()
                c[k] +=1
    bfs(0,[])
    return ret


ls = [1,1,1,2,2]
print(permutate(ls))