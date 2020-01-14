package main

import (
    "fmt"
)

var arr [10]int = [10]int{1,3,2,6,5,6,7,2,4,0}

func bubbleSort(arr [10]int) {
    var n = len(arr)
    swapped := true
    for swapped {
        swapped = false
        for i := 1; i < n; i++ {            
            if arr[i-1] > arr[i] {
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = true
            }
        }
    }
    fmt.Println(arr)
}

func insertionSort(arr [10]int) {
    var n = len(arr)
    for i := 1; i < n; i++ {
        j := i
        for j > 0 {
            if arr[j-1] > arr[j] {
                arr[j-1], arr[j] = arr[j], arr[j-1]
            }
            j = j - 1
        }
	fmt.Println(arr)
    }
    fmt.Println(arr)
}

func main() {
    fmt.Println(arr)
    
    insertionSort(arr)
}