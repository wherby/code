package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

var p = fmt.Println
var pf = fmt.Printf

func main() {
	pt := point{1, 2}

	pf("struct1: %v\n", pt)
	pf("struct2: %+v\n", pt)
	pf("struct3: %#v\n", pt)

	pf("type: %T\n", pt)
	pf("bool: %t\n", true)
	pf("bool: %t\n", pt)
	pf("int: %d\n", 123)
	pf("bin: %b\n", 14)
	pf("char: %c\n", 33)
	pf("hex: %c\n", 456)
	pf("float: %f\n", 78.9)

	pf("float2: %e\n", 1234000000.0)
	pf("float3: %e\n", 1234000000.1)
	pf("str1: %s\n", "\"string\"")
	pf("str2: %q\n", "\"string\"")
	pf("str3: %x\n", "hex this")

	pf("pointer: %p\n", &pt)
	pf("width1: |%6d|%6d|\n", 12, 345)
	pf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)
	pf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)
	pf("width4: |%6s|%6s|\n", "foo", "b")
	pf("width5: |%-6s|%-6s|\n", "foo", "ba")
	s := fmt.Sprintf("sprintf:a %s", "string")
	pf(s)

	fmt.Fprintf(os.Stderr, "io: an %s \n", "error")
}
