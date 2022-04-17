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
ups=[[1,50,20],[20,51,39],[50,70,100],[20,100,230]]
for up in ups:
	a,b,x = up
	sgs=updateSeg(a,b,x,sgs)
print(sgs)