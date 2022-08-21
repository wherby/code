def appendzero(s):
  return s + '0' * len(s)

def expand(s):
  return s + s

def P(k):
  if k == 0:
      return ['1']
  seq = P(k - 1)
  seq_with_zero = [appendzero(s) for s in seq]
  #print("11:",seq_with_zero)
  seq_with_copy = [expand(s) for s in seq]
  #print("22: ", seq_with_copy)
  res = seq_with_copy[:]
  for ins in seq_with_zero:
      res += [ins]
      res += seq_with_copy
  return res

#pls = P(3)
# print(P(0))
# print(P(1))
print(P(2))