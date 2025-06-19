'''
H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

import sys

def solution(citations):
    citations_length = len(citations)

    answer = 0
    for i in range(1, 10_000):

        refer_count = len(list(filter(lambda x : x >= i, citations)))
        if refer_count < i:
            continue

        if citations_length - refer_count > i:
            continue

        answer = max(i, answer)

    return answer

def solution_review(citations):

    citations = sorted(citations)
    citations_length = len(citations)
    for idx, citation in enumerate(citations):
        if citation >= citations_length - idx:
            return citations_length - idx
        
    return 0


questions = [
    [3, 0, 6, 1, 5]
]

result = solution_review(questions[0])
print(result)