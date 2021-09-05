


def dictContains(dic1,dic2):
	isContains = True
	for key,value in dic2.items():
		if key not in dic1:
			isContains = False
			break
		else:
			if value  > dic1[key]:
				isContains = False
				break
	return isContains












dic1 = {"a":3,"b":4,"c":2}
dic2 = {"a":1,"b":2}

print dictContains(dic1,dic2)