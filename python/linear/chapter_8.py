'''
빗물 트래핑
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List
from utils.performance import timer

@timer
def book_solution_1(input:List[int]):

    if len(input) <= 2:
        return 0

    volume = 0
    left, right = 0, len(input) - 1
    left_max, right_max = input[left], input[right]
    '''
    while left < right:
        left_max = max(input[left], left_max)
        right_max = max(input[right], right_max)

        if left_max <= right_max:
            volume += left_max - input[left]
            left += 1
        else:
            volume += right_max - input[right]
            right -= 1
    '''

    while left < right:
        # 매회 마다 왼쪽 벽, 오른쪽 벽 높이를 구한다.
        left_max = max(left_max, input[left])
        right_max = max(right_max, input[right])

        # 높은 쪽에서 낮은 쪽으로 물이 고인다는 생각으로..
        # 왼쪽벽의 높이가 있고, 오른쪽 벽 높이가 있어야. 물 높이가 생길 수 있다.
        # 
        if left_max <= right_max:
            # 현재 높이와 이전까지 가장 높았던 왼쪽 벽 높이 차이를 구한다,
            volume += input[left] - left_max
            left += 1
        else:
            volume += input[right] - right_max
            right_max -= 1
    
    return volume


@timer
def book_solution_2(input:List[int]):#

    stack = []
    volume = 0
    '''
    for i in range(len(input)):

        while stack and input[i] > input[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break
            
            distance = i - stack[-1] - 1
            waters = min(input[i], input[stack[-1]]) - input[top]

            volume += distance * waters

        stack.append(i)
    '''

    for idx in range(len(input)):

        if not stack:
            stack.append(idx)
            continue

        # 현재 검색 된 높이가 이전 높이 보다 크면 고여있을 수 있다.
        curr_height = input[idx]
        while curr_height > input[stack[-1]]:
            stack_top_idx = stack.pop()

            # 욎쪽에 벽에 있어야 한다.
            if not stack:
                break

            # 왼쪽 벽과 오른쪽 벽 사이의 거리
            distance = idx - stack[-1] - 1

            # 오른쪽 벽, 왼쪽 벽, 바닥 으로 인지해야 함 (물이 고일 수 있는 높이 계산)
            waters = min(curr_height, input[stack[-1]]) - input[stack_top_idx]
            volume += waters * distance

            print(f'right: {curr_height}, left: {input[stack[-1]]}, bottom: {input[stack_top_idx]}, waters : {waters}, distance : {distance}')

        stack.append(idx)

    return volume

######

def collect_volume(*, input:List[int], start_idx:int, end_idx:int):
    
    step = 1 if start_idx <= end_idx else -1 

    volume = 0
    enable_put_water_height = -1
    for n in range(start_idx, end_idx, step):
        eanble_volume = enable_put_water_height - input[n]

        if eanble_volume > 0:
            volume += eanble_volume
        else:
            enable_put_water_height = input[n]

    return volume

@timer
def my_solution(input:List[int]):
    
    if len(input) <= 2:
        return 0
    
    left_value, right_value = input[0], input[len(input) - 1]
    left_idx, right_idx = 0, len(input) - 1
    
    left_pivot_idx = 0
    while left_idx < len(input):
        if input[left_idx] > left_value:
            left_value = input[left_idx]
            left_pivot_idx = left_idx
    
        left_idx += 1

    right_pivot_idx = 0
    while right_idx > 0:
        if input[right_idx] > right_value:
            right_value = input[right_idx]
            right_pivot_idx = right_idx

        right_idx -= 1

    # 역전이 발생했으면 값 교체
    if left_pivot_idx > right_pivot_idx:
        left_pivot_idx, right_pivot_idx = right_pivot_idx, left_pivot_idx

    # 0 ~ left_pivot_idx
    volume = collect_volume(
        input=input,
        start_idx=0,
        end_idx=left_pivot_idx
    )

    # left_pivot_idx ~ right_pivot_idx
    volume += collect_volume(
        input=input,
        start_idx=left_pivot_idx,
        end_idx=right_pivot_idx
    )

    # right_pivot_idx ~ max
    volume += collect_volume(
        input=input,
        start_idx=len(input) - 1,
        end_idx=right_pivot_idx
    )

    return volume

if __name__ == '__main__':

    questions = [
        #[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], # 정답 : 6
        [2, 1, 0, 1, 3 ], # 정답 : 4
        [3, 0, 2, 0, 4], # 정답 : 3 + 1 + 3 = 7
        [1, 0, 2, 1, 0, 1], # 정답 : 1 + 0 + 1 + 0 = 2
        [4, 2, 0, 3, 2, 5], # 정답 : 2 + 4 + 1 + 2 = 9
        [0, 1, 0, 2, 1], # 정답 : 1
        [4, 2], # 정답 : 0
        [0, 2, 0, 0, 2, 0, 0], # 정답 : 4
        [0], # 정답 : 0
        [], # 정답 : 0
    ]

    for question in questions:
        #print(f'{book_solution_1(question)}')
        print(f'{book_solution_2(question)}')
        #print(f'{my_solution(question)}')
        break