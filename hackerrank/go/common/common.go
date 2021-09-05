package common

func maxLs(ls []int) int{
	var maxV = ls[0]
	for _,v := range ls{
		if v >maxV{
			maxV = v
		}
	}
	return maxV
}
func minLs(ls []int) int{
	var minV = ls[0]
	for _,v := range ls{
		if v <minV{
			minV = v
		}
	}
	return minV
}