package main

import "fmt"

func main() {
	var a [5]int
	fmt.Println("emp:", a)

	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])
	fmt.Println("len:", len(a))
	fmt.Println(a)

	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	b = [...]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	b = [...]int{100, 3: 400, 500}
	fmt.Println("idx:", b)

	var two [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			two[i][j] = i + j
		}
	}

	fmt.Println("2d: ", two)

	two = [2][3]int{
		{1, 2, 3},
		{1, 2, 3},
	}
	fmt.Println("2d :", two)
	dwarfs1 := []string{"Ceres", "Pluto", "Haumea", "Makemake", "Eris"}
	dwarfs2 := append(dwarfs1, "Orcus")
	dwarfs3 := append(dwarfs2, "Salacia", "Quaoar", "Sedna")
	dwarfs2[4] = "test2"
	dwarfs4 := append(dwarfs3, "Salacia2", "Quaoar2", "Sedna2")
	println(dwarfs1, dwarfs2, dwarfs3)
	dwarfs1[2] = "ts1"
	dwarfs3[3] = "cc1"
	dwarfs4[10] = "cc3"
	fmt.Printf("drarfs1: %v\n", dwarfs1)
	fmt.Printf("drarfs2: %v\n", dwarfs2)
	fmt.Printf("drarfs3: %v\n", dwarfs3)
	fmt.Printf("drarfs4: %v\n", dwarfs4)
	fmt.Println("aa", dwarfs1, dwarfs4)
	println(dwarfs2, dwarfs4)
	planets := []string{
		"Mercury", "Venus", "Earth", "Mars",
		"Jupiter", "Saturn", "Uranus", "Neptune",
	}
	terrestrial2 := planets[0:4]
	worlds2 := append(terrestrial2, "Ceres22")
	terrestrial := planets[0:4:4]
	worlds := append(terrestrial, "Ceres")

	fmt.Println(planets, worlds, terrestrial, worlds2)
}
