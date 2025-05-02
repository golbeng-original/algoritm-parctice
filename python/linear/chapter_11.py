'''
자신을 제외한 배열의 곱
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List
from utils.performance import timer

@timer
def book_solution(input:List[int]):
    if len(input) <= 1:
        return []

    p = 1
    outs = []
    for i in range(len(input)):
        outs.append(p)
        p = p * input[i]

    p = 1
    for i in range(len(input) -1, -1, -1):
        outs[i] = outs[i] * p
        p = p * input[i]

    return outs


@timer
def my_solution(input:List[int]):
    
    if len(input) <= 1:
        return []
    
    p = 1
    left_multiples = []
    for i in range(len(input)):
        left_multiples.append(p)
        p = p * input[i]

    p = 1
    right_multiple = []
    for i in range(len(input) - 1, -1, -1):
        right_multiple.append(p)
        p = p * input[i]

    right_multiple.reverse()

    return [left_multiples[i] * right_multiple[i] for i in range(len(left_multiples))]

'''
[1, 2, 3, 4] <- input
[1, 1, 2, 6] <- 왼쪽 곱 (자기보다 왼쪽만 곱한 값)
[24, 12, 4, 1] <- 오른쪽 곱 (자기보다 오른쪽만 곱한 값)

left 곱 기준 자기보다 왼쪽 수들의 곱
[0] = X             <- X                * ( [1] * [2] * [3] )
[1] = 1             <- [0]              * ( [2] * [3] )
[2] = 1 * 2         <- [0] * [1]        * ( [3] )
[3] = 1 * 2 * 3     <- [0] * [1] * [2]  * ( X )

right 곱 기준 자기보다 오른쪽 수들의 곱
[0] = 2 * 3 * 4     <- [1] * [2] * [3]
[1] = 4 * 3         <- [2] * [3]
[2] = 4             <- [3]
[3] = X             <- X

[0] = X                * ( [1] * [2] * [3] )
[1] = [0]              * ( [2] * [3] )
[2] = [0] * [1]        * ( [3] )
[3] = [0] * [1] * [2]  * ( X )
'''

if __name__ == '__main__':
    
    qustions = [
        [1, 2, 3, 4], # 정답 : [24, 12, 8, 6]
        [0, 1, 2, 3], # 정답 : [6, 0, 0, 0]
        [1, 0, 0, 3], # 정답 : [0, 0, 0, 0]
        [1] # 정답 : []
    ]

    for question in qustions:
        print(f'{question} => {my_solution(question)}')

