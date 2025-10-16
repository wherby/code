# visit my repo: https://github.com/Yawn-Sean/Daily_CF_Problems
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/D?source=facebook
standard_input, packages, output_together = 1, 1, 0
dfs, hashing, read_from_file = 1, 0, 1
de = 1
 
if 1:
 
    if standard_input:
        import io, os, sys
        input = lambda: sys.stdin.readline().strip()
 
        import math
        inf = math.inf
 
        def I():
            return input()
        
        def II():
            return int(input())
 
        def MII():
            return map(int, input().split())
 
        def LI():
            return input().split()
 
        def LII():
            return list(map(int, input().split()))
 
        def LFI():
            return list(map(float, input().split()))
 
        def GMI():
            return map(lambda x: int(x) - 1, input().split())
 
        def LGMI():
            return list(map(lambda x: int(x) - 1, input().split()))
 
    if packages:
        from io import BytesIO, IOBase
 
        import random
        import os
 
        import bisect
        import typing
        from collections import Counter, defaultdict, deque
        from copy import deepcopy
        from functools import cmp_to_key, lru_cache, reduce
        from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest, heapreplace
        from itertools import accumulate, combinations, permutations, count, product
        from operator import add, iand, ior, itemgetter, mul, xor
        from string import ascii_lowercase, ascii_uppercase, ascii_letters
        from typing import *
        BUFSIZE = 4096
 
    if output_together:
        class FastIO(IOBase):
            newlines = 0
 
            def __init__(self, file):
                self._fd = file.fileno()
                self.buffer = BytesIO()
                self.writable = "x" in file.mode or "r" not in file.mode
                self.write = self.buffer.write if self.writable else None
 
            def read(self):
                while True:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    if not b:
                        break
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines = 0
                return self.buffer.read()
 
            def readline(self):
                while self.newlines == 0:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    self.newlines = b.count(b"\n") + (not b)
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines -= 1
                return self.buffer.readline()
 
            def flush(self):
                if self.writable:
                    os.write(self._fd, self.buffer.getvalue())
                    self.buffer.truncate(0), self.buffer.seek(0)
 
        class IOWrapper(IOBase):
            def __init__(self, file):
                self.buffer = FastIO(file)
                self.flush = self.buffer.flush
                self.writable = self.buffer.writable
                self.write = lambda s: self.buffer.write(s.encode("ascii"))
                self.read = lambda: self.buffer.read().decode("ascii")
                self.readline = lambda: self.buffer.readline().decode("ascii")
 
        sys.stdout = IOWrapper(sys.stdout)
 
    if dfs:
        from types import GeneratorType
 
        def bootstrap(f, stk=[]):
            def wrappedfunc(*args, **kwargs):
                if stk:
                    return f(*args, **kwargs)
                else:
                    to = f(*args, **kwargs)
                    while True:
                        if type(to) is GeneratorType:
                            stk.append(to)
                            to = next(to)
                        else:
                            stk.pop()
                            if not stk:
                                break
                            to = stk[-1].send(to)
                    return to
            return wrappedfunc
 
    if hashing:
        RANDOM = random.getrandbits(20)
        class Wrapper(int):
            def __init__(self, x):
                int.__init__(x)
 
            def __hash__(self):
                return super(Wrapper, self).__hash__() ^ RANDOM
 
    if read_from_file:
        file = open("input.txt", "r").readline().strip()[1:-1]
        fin = open(file, 'r')
        input = lambda: fin.readline().strip()
        output_file = open("output.txt", "w")
        def fprint(*args, **kwargs):
            print(*args, **kwargs, file=output_file)
 
    if de:
        def debug(*args, **kwargs):
            print('\033[92m', end='')
            print(*args, **kwargs)
            print('\033[0m', end='')
 
    fmax = lambda x, y: x if x > y else y
    fmin = lambda x, y: x if x < y else y
 
    class lst_lst:
        def __init__(self, n) -> None:
            self.n = n
            self.pre = []
            self.cur = []
            self.notest = [-1] * (n + 1)
        
        def append(self, i, j):
            self.pre.append(self.notest[i])
            self.notest[i] = len(self.cur)
            self.cur.append(j)
        
        def iterate(self, i):
            tmp = self.notest[i]
            while tmp != -1:
                yield self.cur[tmp]
                tmp = self.pre[tmp]

t = II()
outs = []

def euler_tour(n, m, us, vs):
    m = len(us)
    path = [[] for _ in range(n)]
    for edge_id in range(m):
        u = us[edge_id]
        v = vs[edge_id]
        path[u].append(edge_id)
        path[v].append(edge_id)
    vis = [0] * m

    ans = []
    
    for node in range(n):
        if path[node]:
            stack = [node]
            circle = [node]
            circle_rev = []
            while stack:
                u = stack.pop()
                if u < 0:
                    u = ~u
                    while circle[-1] != u:
                        circle_rev.append(circle.pop())
                while len(path[u]) and vis[path[u][-1]]:
                    path[u].pop()
                if len(path[u]):
                    stack.append(~u)
                    edge_id = path[u].pop()
                    vis[edge_id] = 1
                    a, b = us[edge_id], vs[edge_id]
                    if a == u: v = b
                    else: v = a
                    stack.append(v)
                    circle.append(v)

            circle.extend(reversed(circle_rev))
            ans.append(circle)
    
    return ans

for tid in range(1, t + 1):
    n, m = MII()
    deg = [0] * n
    
    us = []
    vs = []
    for _ in range(m):
        u, v = GMI()
        deg[u] += 1
        deg[v] += 1
        us.append(u)
        vs.append(v)
    
    cur = -1
    
    for i in range(n):
        if deg[i] % 2:
            if cur != -1:
                us.append(cur)
                vs.append(i)
                cur = -1
            else:
                cur = i
    
    col = [1] * len(us)
    vis = defaultdict(list)
    for i, (x, y) in enumerate(zip(us, vs)):
        if x > y:
            x, y = y, x
        vis[(x, y)].append(i)
    
    for tour in euler_tour(n, m, us, vs):
        eids = []
        
        for i in range(1, len(tour)):
            u = tour[i - 1]
            v = tour[i]
            if u > v:
                u, v = v, u
            eids.append(vis[(u, v)].pop())
        
        if len(eids) % 2 == 0:
            for eid in eids[::2]:
                col[eid] = 2
        elif max(eids) >= m:
            v = eids.index(max(eids))
            eids = eids[v+1:] + eids[:v]
            for eid in eids[::2]:
                col[eid] = 2
        else:
            u = tour[0]
            for x in tour:
                if deg[x] < deg[u]:
                    u = x
            
            v = eids.index(u)
            eids = eids[v+1:] + eids[:v]
            for eid in eids[::2]:
                col[eid] = 2
    
    check = [0] * n
    for i in range(m):
        if col[i] == 1:
            check[us[i]] += 1
            check[vs[i]] += 1
    
    ans = 0
    for i in range(n):
        vx = check[i]
        vy = deg[i] - check[i]
        
        ans += vx * vx + vy * vy
    
    outs.append(f'Case #{tid}: {ans} {"".join(map(str, col[:m]))}')
    print(f'Case {tid} finished')

fprint('\n'.join(outs))