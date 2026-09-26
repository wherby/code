# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0819/solution/cf104544a.md
# algorithm/codeforce/技巧/对称等价性/枚举可能的中间点.py

import math 
def factors(x):
    for i in range(1, 100000):
        if i * i > x: break
        if x % i == 0:
            yield i
            if x // i != i:
                yield x // i

print(list(factors(1080)))