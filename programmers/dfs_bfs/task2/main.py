'''
네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''

from typing import List, Set
import collections

def solution(n:int, computers:List[List[int]]):

    graph = collections.defaultdict(list)
    for i, e in enumerate(computers):
        for j, connect_value in enumerate(e):
            if i == j or connect_value == False:
                continue

            graph[i].append(j)

    answer = 0
    visited:Set[int] = set()
    for computer_idx in range(len(computers)):
        
        if computer_idx in visited:
            continue

        queue = [computer_idx]
        while queue:
            curr_computer_idx = queue.pop(0)
            if curr_computer_idx in visited:
                continue

            visited.add(curr_computer_idx)
            for next_computer_idx in graph[curr_computer_idx]:
                queue.append(next_computer_idx)

        answer += 1

    return answer

result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
#result = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

print(result)

