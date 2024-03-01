package main

import (
	"fmt"
	"math/rand/v2"
	// "reflect"
)

func main() {
	fmt.Print("Start\n")
	A := populateArray()
	B := populateArray()

	// a method which would technically be correct but might not be what the question inteded would be to truncate one of the arrays by a random small value
	for len(B) == len(A) {
		B = populateArray()
	}
	fmt.Print(A)
	fmt.Print("\n")
	A = shellSort(A)
	fmt.Print(A)
}

func populateArray() (array_Rand []uint16) {
	var len_of_Array uint16 = uint16(rand.Int32N(100) + 256)
	var i uint16 = 0
	array_Rand = make([]uint16, len_of_Array)
	for i = 0; i < len_of_Array; i++ {
		array_Rand[i] = uint16(rand.Int32N(1024))
	}
	return array_Rand
}

func shellSort(unsorted_array []uint16) (sorted_array []uint16) {
	var len_of_Array uint16 = uint16(len(unsorted_array))

	for gap := uint16(len_of_Array / 2); gap > 0; gap-- {
		for counter := uint16(0); counter+gap < len_of_Array; counter++ {
			if unsorted_array[gap+counter] < unsorted_array[counter] {
				hold := unsorted_array[counter]
				unsorted_array[counter] = unsorted_array[gap+counter]
				unsorted_array[gap+counter] = hold
			}
		}

	}
	return unsorted_array
}

// func quickSort(unsorted_array []uint16)(sorted_array []uint16){
// 	var pivot uint16 = uint16(len(unsorted_array)-1)

// }
