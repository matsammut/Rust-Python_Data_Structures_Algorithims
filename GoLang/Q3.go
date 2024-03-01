package main

import (
	"fmt"
	"strings"
)

func q3(){
	A := populateArray()
	Extreme := []int{}
	len_Array := len(A)
	for i := 0; i < len(A); i++ {
		if 0 < A[i] && A[i] < uint16(len_Array-1) && (A[i-1] < A[i] && A[i] > A[i+1] || A[i-1] > A[i] && A[i] < A[i+1]) {
			Extreme = append(Extreme, int(A[i]))
			strings.SplitN()
		}
	}

	if len(Extreme) > 0 {
		fmt.Print("The extreme points are:")
		fmt.Print(Extreme)
	} else {
		fmt.Print("SORTED")
	}

}
