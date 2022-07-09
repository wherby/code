class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tire ={}
        for word in dictionary:
            t = tire
            for ch in word:
                if ch not in t:
                    t[ch] ={}
                t= t[ch]
            t["#"] = "#"
        
        def process(word):
            t =tire
            for i,ch in enumerate(word):
                if ch not in t :
                    break
                t = t[ch]
                if "#" in t :
                    return word[:i+1]
            return word
        return " ".join(map(process,sentence.split(" ")))
            