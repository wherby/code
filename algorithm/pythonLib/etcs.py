ls = [1,2,3,4,5]
for i,a in enumerate(ls,1):
    print(i,a)

import itertools
pres = list(itertools.accumulate(ls,initial=0))
print(pres)