

# 得到段落所有单词
https://leetcode-cn.com/problems/most-common-word/

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word.lower() for word in re.findall(r'[a-zA-Z]+', paragraph)]
        word_map = sorted(collections.Counter(words).items(), key=lambda x: x[1], reverse=True)
        for word, _ in word_map:
            if word not in banned:
                return word

# aho-corosick
https://wherby.github.io/code/string/aho_corasick.html


# Zfunction 前缀字符串匹配


# Manachers 查找一个字符串的子串是否为回文

algorithm/string/manachers/check-if-dfs-strings-are-palindromes.py

用StringHash algorithm/string/manachers/check-if-dfs-strings-are-palindromes3.py

# 对于反转操作的中心扩展法
https://leetcode.cn/problems/minimum-steps-to-convert-string-with-operations/solutions/3695734/hua-fen-xing-dp-tan-xin-pythonjavacgo-by-17kb/
