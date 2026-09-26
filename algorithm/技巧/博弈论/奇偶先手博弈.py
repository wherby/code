# https://leetcode.cn/problems/stone-game-ix/description/
# 如果没有余数为0 的， 则只有一种路径 AABABAB...
# 如果A，B 都有，则先手一定能 选到 数目少的开始，AABAB 然后 A没了，只能选B
# 如果有余数为0 的，ALice选多的那个，因为路径一定是偶数个(增加了一个0)，则如果差值不大于2的时候，Bob可以通过耗尽选择获胜

from typing import List, Tuple, Optional
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        ls = [0]*3
        for s in stones:
            ls[s%3] +=1
        if ls[0]%2==0:
            return ls[1]>0 and ls[2]>0
        else:
            return abs(ls[1]-ls[2])>2