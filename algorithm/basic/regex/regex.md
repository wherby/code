# https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/submissions/ 
class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.replace(' ', '  ')
        sentence = ' ' + sentence + ' '
        # print(re.findall(r' [a-z]+-[a-z]+[!,.]? | [a-z]+[!,.]? ', sentence))
        return len(re.findall(r' [a-z]+-[a-z]+[!,.]? | [a-z]+[!,.]? | [!,.] ', sentence))

class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(bool(re.match(r'[a-z]*([a-z]-[a-z]+)?[!.,]?$', w)) for w in sentence.split())