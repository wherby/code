# 利用set 和排序 去重，利用 b_list[-1]*len(b_list) 的上限来剪枝
# 同理，小猫下山？

def allCombination(ls,N):
    S = {tuple()}

    for x in ls:
        T = set()
        for a_tuple in S:
            a_list = list(a_tuple)
            for j in range(len(a_list)):
                b_list = list(a_list)
                b_list[j] += x 
                b_list.sort()

                if  b_list[-1]*len(b_list)<=N:
                    T.add(tuple(b_list))
            a_list.append(x)
            a_list.sort()
            if  a_list[-1]*len(a_list)<=N:
                T.add(tuple(a_list))
        S = T
    return S

import random

ls = []
for i in range(10):
    ls.append(random.randint(1,20))
for i in range(40):
    ls.append(random.randint(1,2))
ls = [11, 7, 8, 6, 2, 13, 4, 18, 16, 8, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1]
#print(ls,sum(ls))

S = allCombination(ls,sum(ls))
print(S)