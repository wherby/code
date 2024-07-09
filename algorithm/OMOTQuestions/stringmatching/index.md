# String matching

https://leetcode.cn/contest/weekly-contest-405/
https://leetcode.cn/problems/construct-string-with-minimum-cost/description/

## Trie + dp
如果直接用Trie和DP则会超时
如果target 是 a*500000, words={"a","aa","a"*30000} 构造这样的结果，则会产生N**2复杂度
```
class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd =False
        self.cnt = 0
    
    def insert(self,word):
        node = self
        self.cnt +=1
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
            node.cnt +=1
        node.isEnd = True
        
    def find(self,ch):
        ch = ord(ch) - ord('a')
        return self.children[ch]
    
    
    def dfs(self,word,start):
        if start == len(word):
            return True
        node =self
        for i in range(start,len(word)):
            node = node.children[ord(word[i]) -ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word,i +1):
                return True
        return False

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tr = Trie()
        for word  in words:
            tr.insert(word)
        
        dic = {}
        for w,c in zip(words,costs):
            dic[w]= min(c,dic.get(w,10**10))
        #print(dic)
        n = len(target)
        @cache
        def dfs(i):
            if i == n:
                return 0
            tr1 = tr
            j = i
            ret = 10**10
            while tr1 != None and j <n:
                tr1 = tr1.find(target[j])
                j+=1
                if tr1 != None and tr1.isEnd==True:
                    ret = min(ret,dic[target[i:j]] + dfs(j))
            return ret
        ret = dfs(0) 
        return ret if ret<10**10 else -1   
```

###
题目的限制是 "所有 words[i].length 的总和小于或等于 5 * 104" 则一定length和count有一定限制
```
1 <= target.length <= 5 * 104
1 <= words.length == costs.length <= 5 * 104
1 <= words[i].length <= target.length
所有 words[i].length 的总和小于或等于 5 * 104
target 和 words[i] 仅由小写英文字母组成。
1 <= costs[i] <= 104
```

则可以用stringhash 来枚举所有长度下的dp可能

### 
如果用