'''
게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

import heapq
import collections
from typing import Dict, List, Set, Tuple

def solution(maps):

    max_size = (len(maps[0]), len(maps))
    end_point = (max_size[0] - 1, max_size[1] - 1)

    neighbor_rel_points = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    queue = [(1, (0, 0))]

    answer = -1
    visited:Set[Tuple[int, int]] = set()
    while queue:

        distance, point = heapq.heappop(queue)
        if point in visited:
            continue

        if point[0] == end_point[0] and point[1] == end_point[1]:
            answer = distance
            break

        visited.add(point)

        for neighbor_rel_point in neighbor_rel_points:
            
            neighbor_point = (point[0] + neighbor_rel_point[0], point[1] + neighbor_rel_point[1])
            if neighbor_point[0] < 0 or neighbor_point[0] >= max_size[0]:
                continue

            if neighbor_point[1] < 0 or neighbor_point[1] >= max_size[1]:
                continue

            if maps[neighbor_point[1]][neighbor_point[0]] == 0:
                continue

            heapq.heappush(queue, (distance + 1, neighbor_point))

    return answer

result = solution(
    [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
)

#result = solution(
#    [[1], [1]]
#)

print(result)