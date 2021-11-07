class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text = text.lower()
        text = text.split(" ")
        text = sorted(text,key=lambda x: len(x))
        text=" ".join(text)
        text = text[0].capitalize() + text[1:]
        print(text)
        return text

re =Solution().arrangeWords("Keep calm and code on")