package main

import (
	"fmt"
	"time"
)

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("send job", j)
		time.Sleep(time.Millisecond)
	}

	close(jobs)
	fmt.Println("send all jobs")

	<-done
	_, ok := <-jobs
	fmt.Println("received more jobs:", ok)
}
