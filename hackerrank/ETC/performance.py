def formLowerLevel(dic,q):
	global RMQ,ISRMQ
	keys = dic.keys()
	keys = sorted(keys)
	if len(keys) !=q:
		ISRMQ = False
		return (dic,1)
	newDic = removeLowerLevel(dic,keys)
	newKeys= sorted(newDic.keys())
	if len(newKeys) !=q/2:
		ISRMQ = False
		return (newDic,1)
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2] = newKeys[i]
		keys.remove(newKeys[i])   # will timeout for remove element from list
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2 +1] =keys[i]
	return (newDic,q/2)



def formLowerLevel(dic,q):
	global RMQ,ISRMQ,qn
	keys = dic.keys()
	keys = sorted(keys)
	keyVisted=[]
	if len(keys) !=q:
		ISRMQ = False
		return (dic,1)
	newDic = removeLowerLevel(dic,keys)
	newKeys= sorted(newDic.keys())

	if len(newKeys) !=q/2:
		ISRMQ = False
		return (newDic,1)
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2] = newKeys[i]
		keyVisted.append(newKeys[i])
	keyVisted = set(keyVisted)                            #
	keys2 = filter(lambda x: x not in keyVisted, keys)    # will not timeout
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2 +1] =keys2[i]

	return (newDic,q/2)