import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Dict, List, Tuple
from collections import defaultdict
from utils.performance import timer

from typing import TypedDict

class Question(TypedDict):
    nums:List[int]
    target:int

'''
두수의 합
'''

@timer
def book_solution_1(input:Question) -> List[int]:
    nums = input.get('nums')
    target = input.get('target')

    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [i, nums.index(complement, i + 1)]

@timer
def book_solution_2(input:Question) -> List[int]:
    nums = input.get('nums')
    target = input.get('target')

    num_map = {}
    for i, n in enumerate(nums):
        num_map[n] = i

    for i, n in enumerate(nums):
        complement = target - n
        if complement in num_map and i != num_map[complement]:
            return [i, num_map[complement]]

@timer
def book_solution_3(input:Question) -> List[int]:
    nums = input.get('nums')
    target = input.get('target')

    nums.sort()
    
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return None

@timer
def my_solution(input:Question) -> List[int]:
    
    nums = input.get('nums')
    target = input.get('target')

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

if __name__ == '__main__':
    inputs = [
        Question(nums=[2, 7, 11, 15], target=9), # 정답 : [0, 1]
        Question(nums=[3, 2, 4], target=6), # 정답 : [1, 2]
        Question(nums=[3, 3], target=6), # 정답 : [0, 1]
        Question(nums=[1, 2, 3, 4, 5], target=8), # 정답 : [2, 4]
        Question(nums=[1, 2, 3, 4, 5], target=10), # 정답 : [4, 5]
    ]

    for input in inputs:
        print(book_solution_3(input))
        #print(book_solution_2(input))
        #print(book_solution_1(input))
        #print(my_solution(input))