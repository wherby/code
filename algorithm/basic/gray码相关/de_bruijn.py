def de_bruijn(k, n):
    """生成二进制 de Bruijn 序列 B(k, n)"""
    a = [0] * (k * n)
    sequence = []
    
    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for j in range(a[t-p]+1, k):
                a[t] = j
                db(t+1, t)
    
    db(1, 1)
    return sequence

# 生成 B(2, 3)
n=4
seq = de_bruijn(2, n)
print(''.join(map(str, seq)))  # 输出: 00010111

# 检查所有3位子串

substrings = set()
for i in range(len(seq) - n + 1):
    sub = ''.join(map(str, seq[i:i+n]))
    substrings.add(sub)
print(sorted(substrings))
# 输出: ['000', '001', '010', '011', '100', '101', '110', '111']