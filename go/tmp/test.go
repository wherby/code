package main

import "fmt"

func main() {
	// s := []int{1, 2, 3, 4, 5}
	// for i, v := range s {
	// 	if i == 0 {
	// 		s = s[:3]
	// 		s[2] = 100
	// 	}
	// 	println(i, v)
	// }
	// for i, v := range s {
	// 	println(i, v)
	// }
	for i := 0; i < 5; i++ {
		m := map[int]string{
			0: "a", 1: "a", 2: "a", 3: "a", 4: "a",
			5: "a", 6: "a", 7: "a", 8: "a", 9: "a",
		}
		for k := range m {
			m[k+k] = "x"
			delete(m, k)
			fmt.Println(k)
		}
		fmt.Println(m)
	}
}
