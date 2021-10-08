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


binary search 二分 格式
r = mid,l =mid +1 , mid =(l+r)>>1
r = mid,l =mid -1 , mid=(l +r +1)>>1
https://leetcode-cn.com/problems/find-in-mountain-array/submissions/


parser:
add additional bracket 
# https://www.youtube.com/watch?v=K5nbi0CECjA
# https://leetcode-cn.com/problems/brace-expansion-ii/