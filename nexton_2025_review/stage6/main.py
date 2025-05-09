

from dataclasses import dataclass
import sys
from typing import Dict, List, Set

from collections import defaultdict
import heapq

@dataclass
class DistInfo:
    vertex:int
    weight:int

    def as_tuple_for_queue(self):
        return (self.weight, self.vertex)

@dataclass
class RouteInfo:
    vertices:List[int]
    total_weight:int

    def is_include(self, from_vertex:int, to_vertex:int) -> bool:

        from_v = from_vertex if from_vertex < to_vertex else to_vertex
        to_v = from_vertex if from_vertex > to_vertex else to_vertex

        for i in range(1, len(self.vertices)):
            
            if from_v == self.vertices[i - 1] and \
                to_v == self.vertices[i]:
                return True

        return False

def solution(g_nodes:int, g_from:List[int], g_to:List[int], g_weight:List[int]):
    
    graph:Dict[int, List[DistInfo]] = defaultdict(list)

    for i in range(len(g_from)):

        from_v = g_from[i]
        to_v = g_to[i]
        weight = g_weight[i]

        graph[from_v].append(DistInfo(vertex=to_v, weight=weight))
        graph[to_v].append(DistInfo(vertex=from_v, weight=weight))
    
    def find_path(vertex:int, route:List[int], visited:Set[int], acc_weight:int, result:List[RouteInfo]):
        if vertex == g_nodes:
            result.append(RouteInfo(vertices=route, total_weight=acc_weight))
            return

        for dist_info in graph[vertex]:

            next_vertex = dist_info.vertex
            if next_vertex in visited:
                continue

            find_path(next_vertex, [*route, next_vertex], {*visited, vertex}, acc_weight + dist_info.weight, result)

    result:List[RouteInfo] = []
    find_path(1, [1], {}, 0, result)

    # 가장 짧은 비용 경로들 찾기
    result = sorted(result, key=lambda e : e.total_weight)
    min_wieght = result[0].total_weight
    result = list(filter(lambda e: e.total_weight <= min_wieght, result))

    output:List[str] = []
    for i in range(len(g_from)):

        from_v = g_from[i]
        to_v = g_to[i]

        is_include = False
        for route_info in result:
            is_include = route_info.is_include(from_v, to_v)
            if is_include:
                break
        
        output.append('YES' if is_include else 'NO')

    print(output)

if __name__ == '__main__':
    
    solution(
        g_nodes=5,
        g_from= [1, 2, 3, 4, 5, 1, 5],
        g_to=   [2, 3, 4, 5, 1, 3, 3],
        g_weight=[1, 1, 1, 1, 3, 2, 1]
    )