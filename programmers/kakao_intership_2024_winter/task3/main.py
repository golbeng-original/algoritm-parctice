'''
주사위 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/258709
'''

from typing import List

import itertools
import collections

def get_sum_dice_values(dice:List[List[int]], dice_indices:List[int]):

    sum_list = []

    r = len(dice_indices)
    m = len(dice[0])

    def combination(path:List[int]):
        if len(path) == r:
            
            sum_value = 0
            for i in range(len(path)):
                sum_value += dice[dice_indices[i]][path[i]]

            sum_list.append(sum_value)
            return

        for idx in range(0, m):
            path.append(idx)
            combination(path)
            path.pop()

    combination([])

    return sum_list

def solution(dice:List[List[int]]):
    answer = []

    dice_length = len(dice)
    total_dice_indices = set(range(dice_length))
    r = dice_length // 2

    a_dice_combination = []
    def combination(start:int, n:int, combination_list:List[int]):
        
        if len(combination_list) == r:
            a_dice_combination.append(set(combination_list))
            return 
        
        for i in range(start, n):
            combination_list.append(i)
            combination(i + 1, n, combination_list)
            combination_list.pop()

    combination(0, dice_length, [])

    max_win = 0
    max_win_idx = -1
    for idx, a_dice_indices in enumerate(a_dice_combination):
        
        b_dice_indices = total_dice_indices.difference(a_dice_indices)

        a_dice_sum_values = get_sum_dice_values(dice, list(a_dice_indices))
        b_dice_sum_values = get_sum_dice_values(dice, list(b_dice_indices))

        win_count = 0
        for a_value in a_dice_sum_values:
            for b_value in b_dice_sum_values:
                win_count += 1 if a_value > b_value else 0
        
        if win_count > max_win:
            max_win = win_count
            max_win_idx = idx

    return [ e + 1 for e in a_dice_combination[max_win_idx]]


# 부루트 포스트 방식
def calculate_probability(dice_a:List[List[int]], dice_b:List[List[int]]):
    
    outcomes_a = list(itertools.product(*dice_a))
    outcomes_b = list(itertools.product(*dice_b))

    win = 0
    for outcome_a in outcomes_a:
        sum_a = sum(outcome_a)

        for outcome_b in outcomes_b:
            sum_b = sum(outcome_b)

            if sum_a > sum_b:
                win += 1

    return win

# map을 사용한 주사위 합계에서 등장한 합계 카운트 만들기
def make_map(dice_values):

    depth = len(dice_values)
    sum_map = collections.defaultdict(int)

    def backtracking(arr:List[int], depth_idx:int):
        
        if depth == depth_idx:
            dice_sum = sum(arr)
            sum_map[dice_sum] += 1
            return

        for i in range(6):
            arr.append(dice_values[depth_idx][i])
            backtracking(arr, depth_idx + 1)
            arr.pop()

    backtracking([], 0)

    return sum_map

def solution_review(dice:List[List[int]]):
    n = len(dice)

    max_win = 0
    best_win_dice_indiceis = []
    for a_dice_indicies in list(itertools.combinations(range(n), n // 2)):
        b_dice_indicies = [i for i in range(n) if i not in a_dice_indicies]

        dice_a = [dice[i] for i in a_dice_indicies]
        dice_b = [dice[i] for i in b_dice_indicies]

        dice_map_a = make_map(dice_a)
        dice_map_b = make_map(dice_b)

        win = 0
        for sum_a, count_a in dice_map_a.items():
            for sum_b, count_b in dice_map_b.items():
                
                if sum_a > sum_b:
                    win += count_a * count_b

        #win = calculate_probability(dice_a, dice_b)
        #print(win)

        if win > max_win:
            max_win = win
            best_win_dice_indiceis = a_dice_indicies[:]

    return [e + 1 for e in best_win_dice_indiceis]

result = solution_review(
    [
        [1, 2, 3, 4, 5, 6], 
        [3, 3, 3, 3, 4, 4], 
        [1, 3, 3, 4, 4, 4], 
        [1, 1, 4, 4, 5, 5]
    ]
)

print(result)
