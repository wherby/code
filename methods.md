c253/q4 find the increase sub array
https://leetcode.com/contest/weekly-contest-253/problems/find-the-longest-valid-obstacle-course-at-each-position/

c58/q4 find longest palindromic substring -- manachers
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/Python-O(n)-with-Manacher-explained

c253/q2 using priorityQueue will timeout, use heapq will not

c254/q4 using DSU to get union find https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403930/Python-Union-Find-solution-explained
https://usaco.guide/gold/dsu


bfs for all way search need to use dijkstra way:
contest/c59/q3 https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
need to accumulate ways in array and not put in priority queue. 


dp dfs backtrack bitmap
contst/c256/q3 https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1431829/Python-dynamic-programming-on-subsets-explained

FSM for subarray number https://leetcode.com/problems/distinct-subsequences-ii/discuss/192017
https://leetcode.com/contest/weekly-contest-256/problems/number-of-unique-good-subsequences/


using different sort order contest/c257/q2:
https://leetcode.com/contest/weekly-contest-257/problems/the-number-of-weak-characters-in-the-game/
sorted(properties,key=lambda x : x[0]* -10000000 +x[1])


find gcd of big numbers of big number use offline search 
context/c256/q4 https://leetcode.com/contest/weekly-contest-257/problems/gcd-sort-of-an-array/

If need use global int, need to wraped in reference type. int type can't be used as clousre
context/c258/q4 


DP using end for dp context/c61/q3/t32.py

combinations and permutations mix for all possible no repeated element context/c259/q4/t42.py
# https://docs.python.org/3/library/itertools.html#module-itertools
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/discuss/1471930/Python-Answer-is-not-so-long-explained
        for l in range(len(hot) +1):
            for cand in itertools.combinations(hot,l):
                for perm in itertools.permutations(cand):
                    comb.add("".join(perm))
sub sequcence of one string to string context/c259/q4/t42.py
    def isSubsequence(self,s,t):
        t=iter(t)
        return all(c in t for c in s)


#TDK binary search 二分 格式
r = mid,l =mid +1 , mid =(l+r)>>1
r = mid,l =mid -1 , mid=(l +r +1)>>1
https://leetcode-cn.com/problems/find-in-mountain-array/submissions/
如果要写成
r=mid-1 l=mid 的情况也要转变为 r=mid, l= mid +1  最后return l-1
写成 while l<r 的循环的时候，r的值最好是一个不能取的值:  #https://leetcode-cn.com/problems/maximum-number-of-removable-characters/

https://leetcode-cn.com/problems/longest-duplicate-substring/solution/gong-shui-san-xie-zi-fu-chuan-ha-xi-ying-hae9/
l = mid, r=mid -1  , mid = (l+r+1) >>1  while l <r  


parser:
add additional bracket 
# https://www.youtube.com/watch?v=K5nbi0CECjA
# https://leetcode-cn.com/problems/brace-expansion-ii/ 


# DP don't need to search every case 
questions/c242/q32.py 使用辅助结构直接判断dp[i]转移值


# dic :

 self.m.get(key,None) // getvalue of key or default 
 self.m.pop(last.key)  //delete key from dic

# c264/q2
If use dic in inner iteration will timeout, use array will not.

# comb 
from math import comb
>>> from math import comb
>>> comb(10,2)
45

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

# set
a =set([1,2])
>>> a.discard(3)
>>> a
{1, 2}
>>> a.union(set([2,4]))
{1, 2, 4}
>>> a.add(5)   
>>> a
{1, 2, 5}
>>> a.intersection(set([2,4])) 
{2}
>>> a.difference(set([2,4]))
{1, 5}
>>> a
{1, 2, 5}
>>> a.symmetric_difference(set([2,4]))
{1, 4, 5}
#https://realpython.com/python-sets/

# Python字符串比较和字符串截取很快
questions/c227/q31.py  
https://leetcode-cn.com/problems/largest-merge-of-two-strings/submissions/

# getCobination sum
import functools
get_subsums = lambda nums: functools.reduce(lambda s, x: s | {x + ts for ts in s}, nums, {0})


# hint 
搜寻数字，范围为1000左右，用dp, 10000以上2分

# combination number
>>> from math import comb
>>> comb(10,3)
120