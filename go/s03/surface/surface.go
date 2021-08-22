package main

import (
	"fmt"
	"math"
)

const (
	width, heigh = 600, 300
	cells        = 100
	xyange       = 30.0
	xyscale      = width / 2 / xyange
	zscale       = heigh * 0.4
	angle        = math.Pi / 6
)

var sin30, con30 = math.Sin(angle), math.Cos(angle)

func main() {
	fmt.Printf("<svg xmlns='http://www.w3.org/2000/svg'"+
		"style='stroke:grey;fill:white;stroke-width:0.7'"+
		"width='%d' height='%d'>", width, heigh)
	for i := 0; i < cells; i++ {
		for j := 0; j < cells; j++ {
			ax, ay := corner(i+1, j)
			bx, by := corner(i, j)
			cx, cy := corner(i, j+1)
			dx, dy := corner(i+1, j+1)
			fmt.Printf("<ploygon points='%g,%g,%g,%g,%g,%g,%g,%g'/>\n", ax, ay, bx, by, cx, cy, dx, dy)
		}
	}
	fmt.Println("</svg>")
}

func corner(i, j int) (float64, float64) {
	x := xyange * (float64(i)/cells - 0.5)
	y := xyange * (float64(j)/cells - 0.5)

	z := f(x, y)

	sx := width/2 + (x-y)*con30*xyscale
	sy := heigh/2 + (x+y)*sin30*xyscale - z*zscale
	return sx, sy
}

func f(x, y float64) float64 {
	r := math.Hypot(x, y)
	return math.Sin(r)
}
