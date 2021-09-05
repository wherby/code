import csv

csvFile = open("from.csv", "r")
reader = csv.reader(csvFile)
csvFile2 = open("to.csv",'wb')
writer = csv.writer(csvFile2)

ls=[]
def getValue(x):
    l = x.split(":")
    if len(l)>1:
        return int(l[1])
    else:
        return 0
def getType(inputN,outputN):
    #print inputN,outputN
    if inputN == 0:
        return "A"
    if inputN ==1 and outputN ==1:
        return "B"
    if inputN ==1 and outputN >1:
        return "C"
    if inputN >1 and outputN ==1:
        return "D"
    if inputN >1 and outputN >1:
        return "E"
    return "F"


def tranform(item):
    tmp = []
    tmp.append(item[0])
    froma = item[0]
    f1 = filter(lambda x: len(x)!=0, froma.split(" "))
    ad1 =""
    tmp.append(ad1)
    tmp.append(len(ad1))
    inSum = sum(map(lambda x : getValue(x),f1))
    tmp.append(inSum)
    toA = item[1]
    tmp.append(toA)
    t1 = filter(lambda x: len(x)!=0, toA.split(" "))
    tmp.append(len(t1))
    outSum = sum(map(lambda x : getValue(x),t1))
    tmp.append(outSum)
    tmp.append(item[2])
    tmp.append(item[3])
    tmp.append(getType(len(f1),len(t1)))
    return tmp

for item in reader:
    tmp = tranform(item)
    ls.append(tmp)
writer.writerows(ls)
csvFile.close()
csvFile2.close()

