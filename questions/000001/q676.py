class MagicDictionary:

    def __init__(self):
        self.dic=defaultdict(list)


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            for i in range(n):
                ts = word[:i] +"_"+word[i+1:]
                self.dic[ts].append(word)
            


    def search(self, searchWord: str) -> bool:
        fd = False
        n = len(searchWord)
        word = searchWord
        for i in range(n):
            ts = word[:i] +"_"+word[i+1:]
            wls = self.dic[ts]
            for a in wls:
                if a != searchWord:
                    fd = True
        return fd

