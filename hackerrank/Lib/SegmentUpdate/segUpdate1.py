def updateSeg(a,b,x,sgs):
	n = len(sgs)
	re = []
	for i in range(n):
		if a == b :
			pass
		sgt = sgs[i]
		xt,yt,xvt = sgt
		if a >= yt or b<=xt:
			re.append(sgt)
		elif a > xt :
			if b >yt:
				re.append([xt,a,xvt])
				re.append([a,yt,xvt+x])
				a = yt
			elif b == yt:
				re.append([xt,a,xvt])
				re.append([a,yt,xvt+x])
			else :
				re.append([xt,a,xvt])
				re.append([a,b,xvt+x])
				re.append([b,yt,xvt])
		elif a ==xt:
			if b >=yt:
				re.append([a,yt,xvt+x])
				a =yt
			else:
				re.append([a,b,xvt+x])
				re.append([b,yt,xvt])
	return re






#Segment update for array
#rangeUpdate range array

sgs=[[1,100,0]]
ups=[[10,20],[50,60],[10,40],[5,15]]#,[5,10],[25,55]]
for up in ups:
	a,b = up
	sgs=updateSeg(a,b,1,sgs)
print sgs