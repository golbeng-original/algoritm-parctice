import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Dict, List, Tuple
from collections import defaultdict
from utils.performance import timer

from typing import TypedDict

'''
빗물 트래핑
'''

@timer
def my_solution(input:List[int]) -> int:
    if not input:
        return 0

    return 0



if __name__ == '__main__':
    inputs = [
        [0,1,0,2,1,0,1,3,2,1,2,4], # 정답 : 6
        [4,2,0,3,2,5], # 정답 : 9
        [1,0,2], # 정답 : 1
        [2,0,2], # 정답 : 2
        [3], # 정답 : 0
        [], # 정답 : 0
    ]

    for input in inputs:
        print(f'input: {input} => my_solution: {my_solution(input)}')