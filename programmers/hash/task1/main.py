'''
완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

import collections

def solution(participant, completion):
    
    participant_map = collections.defaultdict(int)
    for e in participant:
        participant_map[e] += 1

    for e in completion:
        participant_map[e] -= 1

    max_count = -1
    answer = ''
    for k, v in participant_map.items():
        if v > max_count:
            answer = k
            max_count = v

    return answer

def solution_review(participant, completion):

    value = collections.Counter(participant) - collections.Counter(completion)
    return list(value.keys())[0]

result = solution_review(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print(result)