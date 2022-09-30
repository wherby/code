# https://stackoverflow.com/questions/9185768/inverting-permutations-in-python
# https://codeforces.com/contest/1726/problem/E
def inv(perm):
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p] = i
    return inverse

a = [2,1,0]
print(inv(a))