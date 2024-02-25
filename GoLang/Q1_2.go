package main

import (
	// "fmt"
	"math/rand/v2"
	// "reflect"
)

func main() {

	var len_of_A = rand.Int32N(100) + 256

	A := make([]int32, len_of_A)
	var i int32 = 0
	for i = 0; i < len_of_A; i++ {
		A[i] = rand.Int32N(1024)
	}

	len_of_B := rand.Int32N(100) + 256

	B := make([]int32, len_of_B)
	for i = 0; i < len_of_B; i++ {
		B[i] = rand.Int32N(1024)
	}
}

func populateArray() {
	var len_of_A = rand.Int32N(100) + 256
	A := make([]int32, len_of_A)
	var i int32 = 0
	for i = 0; i < len_of_A; i++ {
		A[i] = rand.Int32N(1024)
	}
	return A
}
