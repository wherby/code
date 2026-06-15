# https://codeforces.com/gym/105383/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0610/solution/cf105383c.md
# 逆序对处理
# 因为正面反面序号是对应的，所以用正面的序号编码反面的序号，这样得到的 p是具有逆序对的数组，q是顺序数组，这样的到的p,q和原始的正反面序号是等价的
# 然后利用 自然序列的连续性，在第i位一定能构成 i-1个逆序对的方式，来消除已有的逆序对  rev_pairs -= notes[i] 是如果 p 按照顺序排序能消除的逆序对， for j in range(rev_pairs): 是因为 q[i] 一定比q[0:i]大，这样去构造q的逆序对，来消除p的逆序对
# for j in range(rev_pairs): 我可以保证 q序列增加了rev_pairs个逆序对，我怎么保证 p序列减少了rev_pairs个逆序对呢？
# 因为notes[i] 保证了 i 这个INDEX可以由notes[i]个逆序对，而把p数组的 p[:i] 排序之后，可以知道有 nodes[i]个元素比 p[i] 大，所以把 p[i]往前冒泡 rev_pairs次，也一定能产生对应的逆序对


import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree
def main():
    n = II()
    p1 = LGMI()
    p2 = LGMI()
    
    p = [0] * n
    for i in range(n):
        p[p1[i]] = p2[i]
    
    fen = FenwickTree(n)
    notes = []
    rev_pairs = 0
    
    for x in p:
        notes.append(fen.rsum(x + 1, n - 1))
        rev_pairs += notes[-1]
        fen.add(x, 1)
    
    if rev_pairs % 2:
        print('No')
    else:
        rev_pairs //= 2
        
        q = list(range(n))
        
        for i in range(n):
            if rev_pairs < notes[i]:
                q[:i] = sorted(q[:i], key=lambda x: p[x])
                p[:i] = sorted(p[:i])
                
                for j in range(rev_pairs):
                    p[i - j], p[i - j - 1] = p[i - j - 1], p[i - j]
                    q[i - j], q[i - j - 1] = q[i - j - 1], q[i - j]
                
                break
            else:
                rev_pairs -= notes[i]
        
        print('Yes')
        print(' '.join(str(x + 1) for x in q))
        print(' '.join(str(x + 1) for x in p))

main()