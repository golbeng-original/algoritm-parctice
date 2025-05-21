'''
모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''
import collections

def solution(answers):

    # 각자 tester 별로 찍기 패턴
    tester =[
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    best_score = 0
    scores = collections.defaultdict(list)

    for j in range(3):

        check_tester = tester[j]
        score  = 0
        for i, value in enumerate(answers):
            score += 1 if check_tester[ i % len(check_tester) ] == value else 0

        scores[score].append(j + 1)
        best_score = max(best_score, score)

    return scores[best_score]

result = solution([1,3,2,4,2])
print(result)