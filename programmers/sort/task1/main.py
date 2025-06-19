'''
K번째수
https://school.programmers.co.kr/learn/courses/30/lessons/42748
'''

from typing import List

def solution(array:List[int], commands:List[List[int]]):
    answer = []

    for command in commands:
        i, j, k = command
        
        sub_array = array[i-1:j]
        sub_array.sort()
        answer.append(sub_array[k - 1])

    return answer


questions = [
    ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
]

result = solution(*questions[0])
print(result)