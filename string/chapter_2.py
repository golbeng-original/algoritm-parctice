import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from copy import deepcopy
from typing import List

from utils.performance import timer

'''
문자열 뒤집기
'''

@timer
def my_solution(input:List[str]):
    
    question = deepcopy(input)

    start_idx = 0
    end_idx = len(question) - 1

    while start_idx < end_idx:
        question[start_idx], question[end_idx] = question[end_idx], question[start_idx]
        start_idx += 1
        end_idx -= 1

    return question


if __name__ == '__main__':
    #input = ['h', 'e', 'l', 'l', 'o']
    input = ['H', 'a', 'n', 'n', 'a', 'h']

    result = my_solution(input)
    print(result)