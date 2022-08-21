
from prometheus_client import Counter


def appendzero(s):
  return s + '0' * len(s)

def expand(s):
  return s + s

def P(k):
  if k == 0:
      return ['1']
  seq = P(k - 1)
  seq_with_zero = [appendzero(s) for s in seq]
  seq_with_copy = [expand(s) for s in seq]
  res = seq_with_copy[:]
  for ins in seq_with_zero:
      res += [ins]
      res += seq_with_copy
  return res

pls = P(3)

def resolve():
    x = 2
    while x !=0:
        for k in pls:
            print(k)
            x = int(input())
            if x ==0:
                break
    return True
    
def op(caseidx):
    re= resolve()
    return re
    

for i in range(int(input())):
    re = op(i)
    if re != True:
        break

# import collections
# for p in pls:
    
#     count = collections.Counter(p)
#     print(count["1"])
# print(len(pls))


