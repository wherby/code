# 把多重不同方向的条件 转换为同一方向计算的多重条件
# https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/?envType=daily-question&envId=2025-03-12
# https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/2934309/liang-ci-hua-chuang-pythonjavacgo-by-end-2lpz/
# 恰好型滑动窗口：转换成两个至少型滑动窗口（Python/Java/C++/Go）

# 答：「至少 20 岁」可以分成「恰好 20 岁」和「至少 21 岁」，所以「至少 20 岁」的人数减去「至少 21 岁」的人数，就是「恰好 20 岁」的人数，即 10−3=7。


from collections import defaultdict,deque
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        
        def f(k1):
            acc = 0 
            l = 0 
            cnt = 0
            dic= defaultdict(int)
            for a in word:
                if a in vowls:
                    dic[a] +=1
                else:
                    acc +=1
                while acc >= k1 and all(dic[b] >0 for b in vowls):
                    if word[l] in vowls:
                        dic[word[l]] -=1
                    else:
                        acc -=1
                    l +=1
                cnt +=l 
            return cnt 
        return f(k) -f(k+1)