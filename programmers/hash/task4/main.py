'''
의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''

from typing import Dict, List
import collections
import itertools
import functools  

def solution(clothes:List[List[str]]):

    if len(clothes) > 30:
        return 0

    ordered_clothes:Dict[str, List[str]] = {}
    for cloth in clothes:
        if cloth[1] not in ordered_clothes:
            ordered_clothes[cloth[1]] = []

        ordered_clothes[cloth[1]].append(cloth[0])

    # 의상 조합 idx 조합 찾기
    clothes_names = [k for k in ordered_clothes.keys()]
    closthes_combs = []
    for i in range(len(clothes_names)):
        comb = list(itertools.combinations(clothes_names, i + 1))
        closthes_combs.append(comb)

    answer = 0
    for comb in closthes_combs:
        for comb_element in comb:
            answer += functools.reduce(
                lambda e, acc : e * acc,
                [len(ordered_clothes[e]) for e in comb_element],
                1
            )

    return answer

def solution_review(clothes:List[List[str]]):

    counter = collections.Counter([k for v, k in clothes])

    comb = 1
    for value in counter.values():
        comb *= (value + 1)

    return comb - 1

result = solution_review(
    [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"],
        ["a", "pants"],
        ["b", "pants"],
    ]
)

print(result)