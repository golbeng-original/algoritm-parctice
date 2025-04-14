'''
세수의 합
'''
import sys
import os
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.performance import timer

@timer
def my_solution(input:List[int]):
    
    input.sort()

    result:List[List[int]] =[]

    for i in range(len(input)):

        pivot = input[i]

        left = i+1
        right = len(input) - 1
        while left < right:

            sum = pivot + input[left] + input[right]
            if sum < 0:
                left +=1
            elif sum > 0:
                right -= 1
            else:
                result.append([pivot, input[left], input[right]])
                break

    return result

if __name__ == '__main__':

    questions = [
        [-1, 0, 1, 2, -1, -4], # 정답 : [[-1, -1, 2], [-1, 0, 1]]
        [0, 1, 1], # 정답 : []
        [0, 0, 0], # 정답 : [[0, 0, 0]]
        [-2, 0, 0, 2, 2], # 정답 : [[-2, 0, 2]]
        [-4, -1, -1, 0, 1, 2], # 정답 : [[-4, -1, 2], [-1, -1, 2]]
    ]

    for question in questions:
        print(f'{question} => {my_solution(question)}')