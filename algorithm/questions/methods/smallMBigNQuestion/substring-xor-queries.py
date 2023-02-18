# https://leetcode.cn/contest/weekly-contest-332/problems/substring-xor-queries/
from typing import List, Tuple, Optional
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        def toInt(st):
            acc =0 
            for a in st:
                acc = acc*2+int(a)
            return acc 
        n = len(s)
        dic={}
        for i in range(1,33):
            for j in range(n-i+1):
                s1 = s[j:j+i]
                ac = toInt(s1)
                if ac not in dic:
                    dic[ac] = j
        res =[]
        #print(dic)
        for a,b in queries:
            c = a^b 
            if c in dic:
                clen =len(bin(c))-2
                res.append([dic[c],dic[c] + clen-1])
            else:
                res.append([-1,-1])
            #print(c,res,dic)
        return res
    
    
#第三题：子字符串异或查询
#对于每个 queryquery —— [first_i, second_i][first 
#i
​#
# ,second 
#i
​
# ]，要求 val \textcircled{+} first_i = second_i，实际上也就是 val = first_i \textcircled{+} second_i（其中 \textcircled{+} 表示一个异或，这里是因为x \textcircled{+} y \textcircled{+} y = x）。

#因此我们只需要对一个十进制的数值，在数组种查找是否有其二进制表示即可。而为了使得数组尽可能短，我们可以去掉所有前导 00。

#因为我们去掉了前导 00，我们的子串长度不会超过 3030，因此我们枚举所有长度不超过 3030 的子串，计算其十进制数值，即可得到结果。

#具体代码如下——
#以下代码的复杂度为 \mathcal{O}(n log ^ 2 M)O(nlog 
#2
# M)。

#python

from collections import defaultdict,deque
def getInt(s):
    ans = 0
    for c in s:
        ans *= 2
        ans += int(c)
    return ans

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pos = defaultdict(lambda: [-1, -1]) # 设定默认答案
        n = len(s)
        for i in range(1, 32):
            for j in range(n - i + 1):
                res = getInt(s[j:j+i])
                if res not in pos: pos[res] = [j, j+i-1]
        return [pos[x ^ y] for x, y in queries]
#事实上可以不用直接截取每个字符串以得到十进制数值，
# 可以直接对上一个枚举的字符串去掉最高位再加上新的数位，
# 这样计算十进制数值的复杂度为均摊 \mathcal{O}(1)O(1) 的。

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/ayE0iI/view/ndtcg2/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。