'''
배열 파티션 1
'''
import sys
import os
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.performance import timer

@timer
def book_solution_1(input:List[int]):
    input.sort(reverse=True)
    sum = 0
    for i, n in enumerate(input):
        if i % 2 == 1:
            sum += n

    return sum


@timer
def book_solution_2(input:List[int]):
    return sum(sorted(input, reverse=True)[1::2])

@timer
def my_solution(input:List[int]):
    
    input.sort(reverse=True)
    sum = 0
    for i in range(0, len(input), 2):

        pair = input[i:i+2]
        if len(pair) < 2:
            break

        sum += min(pair)

    return sum

if __name__ == '__main__':

    questions = [
        [1, 4, 3, 2], # 정답 : 4
        [6, 2, 6, 5, 1, 2], # 정답 : 9
        [1, 2], # 정답 : 1
        [1], # 정답 : 0
        [1, 2, 3], # 정답 : 2
    ]

    for question in questions:
       print(f'{question} => {book_solution_2(question)}')
       #print(f'{question} => {book_solution_1(question)}')
       #print(f'{question} => {my_solution(question)}')