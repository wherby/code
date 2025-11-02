# https://leetcode.com/contest/weekly-contest-474/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/description/

import math
INF  = math.inf
from collections import Counter
from string import ascii_lowercase
def nextPermutation(nums) :
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def lexEqualOrGreaterPermutation( s: str, target: str) -> str:
    
    s1 = [ord(a) -ord('a') for a in s]
    s2 = [ord(a) -ord('a') for a in target]
    Equal = True
    n = len(s1)
    c = [0]*26
    for a in s1:
        c[a]+=1
    ret = []
    i=0
    while i<n:
        if Equal:
            b= s2[i]
            if c[b] != 0 :
                c[b] -=1
                ret.append(b)
            else:
                fd = False
                for idx in range(b+1,26):
                    if c[idx] != 0:
                        c[idx] -=1
                        ret.append(idx)
                        fd =True
                        Equal = False
                        break
                if fd == False:
                    for j in range(25,-1,-1):
                        ret.extend([j]*c[j])
                    nextPermutation(ret)
            i=len(ret)

        else:
            for j in range(26):
                if c[j] != 0 :
                    ret.extend([j]*c[j])
            break
    s3 = [chr(a+ord('a')) for a in ret]
    return "".join(s3)

class Solution:



    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(target)
        hf = n //2
        odv = ""
        c = Counter(s)
        left = Counter()
        mxs = []
        for k,v in c.items():
            left[k] = v //2 
            if v%2 ==1:
                if odv != "":
                    return ""
                odv =k
        for j in range(25,-1,-1):
            ch = ascii_lowercase[j]
            mxs.extend(ch * left[ch])
        mxs = "".join(mxs)
        nxs = lexEqualOrGreaterPermutation(mxs,target[:n//2])
        if nxs> target[:n//2]:
            return nxs + odv + nxs[::-1]
        else:
            t1 = nxs + odv + nxs[::-1]
            if t1 > target:
                return t1
            s2 = [a for a in nxs]
            nextPermutation(s2)
            nxs = "".join(s2)
            
            t1 = nxs + odv + nxs[::-1]
            if t1 >target:
                return t1
            else:
                return ""



re =Solution().lexPalindromicPermutation(s = "baba", target = "abaa")
print(re)