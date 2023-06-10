# https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/
from collections import Counter
from itertools import groupby
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = Counter(text)
        groups = [[char, len(list(group))] for char, group in groupby(text)]
        print(groups)
        print([(char, list(group)) for char, group in groupby(text)])
        

re =Solution().maxRepOpt1("aaabbaaa")
