

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