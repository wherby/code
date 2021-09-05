package main

import ("fmt"
)

	
func All(vs []byte, f func(v byte) bool) bool {
    for _, v := range vs {
        if !f(v) {
            return false
        }
    }
    return true
}

func isMatch(s string, p string) bool {
	var  sn = len(s)
	var  pn = len(p)
	arr := make([][]bool,sn+1)
	for i :=0; i< sn+1; i++ {
		arr[i] = make([]bool,pn+1)
	}
	arr[0][0] = true
	for i:=1; i<sn+1;i++ {
		arr[i][0] = false
	}
	for i:=1; i< pn +1 ; i ++{
		arr[0][i] = All([] byte(p[:i]),func(v byte) bool {
			return v =='*'
		})
	}
	for i:=1; i < sn +1; i++ {
		for j :=1; j<pn +1; j++ {
			arr[i][j] = (arr[i-1][j-1] && s[i-1] == p[j-1]) ||
						(arr[i-1][j-1] && '?' ==p[j-1]) ||
						(arr[i-1][j] && '*' ==p[j-1]) ||
						(arr[i][j-1] && '*' ==p[j-1])
		}
	}

	return arr[sn][pn]
}

func main() {

	fmt.Println(isMatch("cb", "?a"))
	fmt.Println(isMatch("adceb","*a*b"))
}

