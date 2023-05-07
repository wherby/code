# https://leetcode.cn/problems/last-substring-in-lexicographical-order/
# 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
# https://leetcode.cn/problems/last-substring-in-lexicographical-order/solution/an-zi-dian-xu-pai-zai-zui-hou-de-zi-chua-31yl/

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]

#作者：LeetCode-Solution
#链接：https://leetcode.cn/problems/last-substring-in-lexicographical-order/solution/an-zi-dian-xu-pai-zai-zui-hou-de-zi-chua-31yl/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。