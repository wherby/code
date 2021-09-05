import csv
import string

csvFile = open("keyValuePairs.csv", "r")
reader = csv.reader(csvFile)
fileWrite = open("tostr.txt","w")
dc = {}
dc["list"] = []

def transform(item):
	global dc
	ls = item.split(",")
	ls =list( map(lambda x : x.strip(string.whitespace).replace("'",""),ls))
	ls = list(filter(lambda x : len(x)>0,ls))
	key={}

	if len(ls) ==3:
		key["chinese_values"] = [ls[0]]
		key["english_values"] = [ls[1]]
		key["key"] = ls[2]
		dc["list"].append(key)
		print(ls)


for item in csvFile:
	transform(item)

fileWrite.write(str(dc))
csvFile.close()
fileWrite.close()
#print(dc)
