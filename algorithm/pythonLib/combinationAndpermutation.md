#TDK itertools  combination and  permutations
>>> ls = [1,2,3,4,5] 
>>> for cand in itertools.combinations(ls,3):
...     print(cand)
... 
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 4)
(1, 3, 5)
(1, 4, 5)
(2, 3, 4)
(2, 3, 5)
(2, 4, 5)
(3, 4, 5)

>>> ls =[1,2,3]
>>> for perm in itertools.permutations(ls):   
...     print(perm)
... 
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)