package main

import (
	"fmt"
)

func listGenerator(pattern []int, size int) []int {
	var output = []int{}
	pattern_length := len(pattern)
	for i:=0; i<size;i++ {
		output = append(output, pattern[i%pattern_length])
	}
	return output
}

func count_same_list(list1 []int, list2 []int, size int) int{
	count := 0
	for i:=0; i<size; i++ {
		if list1[i] == list2[i] {
			count++
		}
	}
	return count
}

func solution(answers []int) []int {

	patterns := [][]int{[]int{1, 2, 3, 4, 5}, []int{2, 1, 2, 3, 2, 4, 2, 5}, []int{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}}
	answer_length := len(answers)

	highest_score_person := []int{}
	max_v := 0
	for i:= 0 ; i < 3; i++ {
		list := listGenerator(patterns[i], answer_length)
		count := count_same_list(answers, list, answer_length)
		if count > max_v {
			max_v = count
			highest_score_person = []int{i+1}

		} else if count == max_v {
			highest_score_person = append(highest_score_person, i+1)
		}
	}

	return highest_score_person
}


func main() {
	fmt.Println(solution([]int{1,3,2,4,2}))
}