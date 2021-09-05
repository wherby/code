#https://leetcode.com/problems/combination-sum-ii/discuss/
#All Combination of candidates num sum for a target. DP


def combinationSum2( candidates, target):
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    for i in candidates:
        if i > target:
            break
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))
    #print table
    return map(list, table[target])


candidates = [10, 1, 2, 7, 6, 1, 5]
print combinationSum2(candidates,8)