#https://www.hackerrank.com/contests/optimization-oct17/challenges/keywords

def minimumLength(text, keys):
    answer = 10000000
    text += " $"
    mxAns = answer
    optAns = len(keys) + sum(map(lambda x: len(x),keys))-1
    dup ={}
    for k1 in keys:
            dup[k1] =1
    alltex = text.split(" ")
    startls = []
    index =0
    for x in alltex:
        if x in dup:
            startls.append(index)
        index = index + 1 + len(x)

    dup = {}
    for i in startls:
        for k1 in keys:
            dup[k1] =1
        word = ""
        if i > 0 and text[i - 1] != ' ':
            continue

        for j in xrange(i, min(len(text),mxAns+i)):
            if text[j] == ' ':
                if word in dup:
                    del dup[word]
                word = ""
            else:
                word += text[j]
            if not len(dup):
                answer = min(answer, j - i)
                mxAns = answer
                if mxAns == optAns:
                    return answer
                break

        if(answer == 10000000):
            answer = -1

    return answer

text = "why how what how when how when what"
keys= ["what","when"]
print minimumLength(text,keys)