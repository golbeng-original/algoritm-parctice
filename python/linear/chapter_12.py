'''
주식을 사고팔기 가장 좋은 시점
'''
import sys
import os
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.performance import timer


@timer
def book_solution_1(input:List[int]):
    profit = 0
    min_price = sys.maxsize

    for price in input:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

@timer
def my_solution(input:List[int]):
    
    # 1순위 idx, 2순위 price
    max_return = 0
    for i in range(len(input)):

        for j in range(i + 1, len(input)):
            if input[i] > input[j]:
                break
                
            max_return = max(max_return, input[j] - input[i])

    return max_return

if __name__ == '__main__':

    questions = [
        [7, 1, 5, 3, 6, 4], # 정답 : 5
        [7, 6, 4, 3, 1], # 정답 : 0
        [2, 4, 1], # 정답 : 2
        [1, 2], # 정답 : 1
        [2, 1], # 정답 : 0
        [1], # 정답 : 0
    ]

    for question in questions:
        print(f'{question} => {book_solution_1(question)}')
        #print(f'{question} => {my_solution(question)}')