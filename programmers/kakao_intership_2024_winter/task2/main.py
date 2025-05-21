import collections

from typing import Dict, List
'''
도넛과 막대 그래프
https://school.programmers.co.kr/learn/courses/30/lessons/258711
'''


def solution(edges:List[List[int]]):
    answer = []

    # 들어오는 간선이 있는 점정
    exist_enter_edge_vertices = set()
    graph:Dict[int, List[int]] = collections.defaultdict(list)
    for lhs, rhs in edges:
        graph[lhs].append(rhs)
        exist_enter_edge_vertices.add(rhs)

    # 생성 정점 찾기
    start_vertex = 0
    max_edges = 0
    for key, value in graph.items():
        if key in exist_enter_edge_vertices:
            continue
        
        if max_edges < len(value):
            start_vertex = key
            max_edges = len(value)


    answer = [start_vertex, 0, 0, 0]

    search_edges = graph[start_vertex]

    for search_edge in search_edges:
        
        vertex_count = 0
        edge_count = 0
        visited_vertex = set()

        stack = []
        stack.append(search_edge)
        while stack:
            vertex = stack.pop(-1)
            if vertex in visited_vertex:
                continue

            vertex_count += 1
            visited_vertex.add(vertex)
            for next_vertex in graph[vertex]:
                edge_count += 1
                stack.append(next_vertex)

        # 막대 모양
        if vertex_count > edge_count:
            answer[2] += 1
        # 8자 모양
        elif vertex_count < edge_count:
            answer[3] += 1
        # 도넛 모양
        else:
            answer[1] += 1

    return answer

result = solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])
print(result)