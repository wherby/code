package main

import ("fmt"
	"os"
	 "bufio"
	 "container/list"
	 "strconv"
	 "strings"
	 )

type Line struct{
	slope,xterm int64
}

func(line *Line) get(x int64) int64{
	return line.slope *x + line.xterm
}

func area(a *Line,b *Line, c *Line) int64{
	var ax =b.slope -a.slope
	var bx = c.xterm - a.xterm
	var ay = c.slope -a.slope
	var by = b.xterm - a.xterm
	return ax * bx - ay *by
}

func cw(a *Line,b *Line, c *Line) bool{
	return area(a,b,c) <0
}

var lines = make([]Line,0)
func insert(l *Line){
	for len(lines) >1 && cw(&lines[len(lines)-2],&lines[len(lines)-1],l){
		lines = lines[:len(lines)-1]
	}
	if len(lines) ==1{
		if(lines[0].xterm > l.xterm){
			lines = append(lines,*l)
		}
	}else{
		lines = append(lines,*l)
	}
}

func query(x int64) int64{
	if len(lines) ==0{
		return 0
	}
	for len(lines)>1 && lines[0].get(x) > lines[1].get(x){
		lines = lines[1:]
	}
	return lines[0].get(x)
}

var MAXN = 5000

var weight= make([]int64, MAXN +5)
var pos = make([]int64, MAXN +5)
var A, B, F  [MAXN+5]int64