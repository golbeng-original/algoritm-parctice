'''
최소직사각형
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''

import sys
from typing import List


def solution(sizes:List[List[int]]):

    # 직사각형에 w, h를 바꿔도 size는 같다.
    # 각 직사각형별로 w,h를 큰 것을 w로 둔다.

    for size in sizes:
        size.sort(reverse=True)

    max_width = -sys.maxsize
    max_height = -sys.maxsize
    for size in sizes:
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])


    return max_width * max_height


result = solution([[60, 50], [30, 70], [60, 30], [80, 40]]) # 4000
print(result)