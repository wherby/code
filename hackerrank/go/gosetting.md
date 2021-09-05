
## set gopath goroot


First run go env.
If you are see that the go insn't installed you can install it via homebrew or via package and/or other ways.
If you are seeing output then your go is installed.
It shows you all the envs that are set and are not.

If you see empty for GOROOT:

run which go (On my computer : /usr/local/go/bin/go)
then export like this  export GOROOT=/usr/local/go
If you see empty for GOPATH:

Create any directory anywhere on your computer for go projects in my case: ~/GO_PROJECTS
then export GOPATH=~/GO_PROJECTS

https://stackoverflow.com/questions/7970390/what-should-be-the-values-of-gopath-and-goroot
