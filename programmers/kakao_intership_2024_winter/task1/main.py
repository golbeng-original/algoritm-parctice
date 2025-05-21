from typing import Dict, List
import collections
'''
가장 많이 받은 선물
https://school.programmers.co.kr/learn/courses/30/lessons/258712
'''
def solution(friends:List[str], gifts:List[str]):

    sender_graph:Dict[str, Dict[str, int]] = {}
    receive_graph:Dict[str, Dict[str, int]] = {}
    for f in friends:
        sender_graph[f] = collections.defaultdict(int)
        receive_graph[f] = collections.defaultdict(int)

    for g in gifts:
        sender, receiver = g.split(' ')
        sender_graph[sender][receiver] += 1
        receive_graph[receiver][sender] += 1

    gift_scores:Dict[str, int] = {}
    for f in friends:
        sender_score = [v for v in sender_graph[f].values()]
        receive_score = [v for v in receive_graph[f].values()]

        gift_scores[f] = sum(sender_score) - sum(receive_score)

    final_gifts:Dict[str, int] = collections.defaultdict(int)
    for f1 in friends:
        for f2 in friends:
            if f1 == f2:
                continue

            if sender_graph[f1][f2] == sender_graph[f2][f1] and \
                gift_scores[f1] > gift_scores[f2]:
                final_gifts[f1] += 1
            
            elif sender_graph[f1][f2] > sender_graph[f2][f1]:
                final_gifts[f1] += 1

    if not final_gifts:
        return 0

    return max(final_gifts.values())


answer = solution(
    ["muzi", "ryan", "frodo", "neo"],
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
)

print(answer)