'''
여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''

import collections
from typing import Dict, List, Set


def solution(tickets:List[List[str]]):
    graph:Dict[str, List[str]] = collections.defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for value in graph.values():
        if len(value) >= 2:
            value.sort()

    def dfs(src:str, remain_ticket:collections.Counter, path:List[str], result:List[str]):
        if len(path) == (len(tickets) + 1):
            result.extend(path)
            return True

        for dest in graph[src]:

            use_ticket = (src, dest)
            if remain_ticket[use_ticket] == 0:
                continue

            remain_ticket.subtract([use_ticket])
            #remain_ticket.remove(use_ticket)
            if dfs(dest, remain_ticket, path + [dest], result):
                return True
            
            remain_ticket.update([use_ticket])

        return False

    remain_ticket = collections.Counter([(ticket[0], ticket[1]) for ticket in tickets])

    answer = []
    dfs('ICN', remain_ticket, ['ICN'], answer)
    return answer

    '''
    queue = ['ICN']
    answer = []
    while queue:
        name = queue.pop(-1)
        answer.append(name)

        dests = graph[name]
        if not dests:
            break

        is_find_dest = False
        
        # 다음 목적지의 목적지가 있는 경우부터 처리
        for idx, dest in enumerate(dests):
            
            if len(graph[dest]) >= 1:
                queue.append(dest)
                del dests[idx]
                is_find_dest = True
                break

        if not is_find_dest:
            queue.append(dests.pop(0))

    return answer
    '''

result = solution([["ICN", "B"], ["B", "ICN"], ["ICN", "B"], ["B", "ICN"]])
# [ICN, B, ICN, B, ICN]
#result = solution([["ICN", "D"], ["D", "ICN"], ["ICN", "B"]])
# ['ICN', 'B', 'D', 'ICN']

#result = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) 
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(result)

# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# ['ICN', 'ATL', 'ICN', 'SFO', 'ATL']