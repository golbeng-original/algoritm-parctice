'''
기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
'''

import math

def solution(progresses, speeds):
    answer = []

    length = len(progresses)

    curr_idx = 0
    while curr_idx != None:
        progress = progresses[curr_idx]
        speed = speeds[curr_idx]

        remain = 100 - progress
        day = remain // speed
        if remain % speed > 0:
            day += 1

        next_idx = None
        for idx in range(curr_idx, length):
            progresses[idx] = progresses[idx] + (speeds[idx] * day)
            if not next_idx and progresses[idx] < 100:
                next_idx = idx
        
        if next_idx:
            answer.append(next_idx - curr_idx)
        else:
            answer.append(length - curr_idx)

        curr_idx = next_idx

    return answer

def solution_review(progresses, speeds):

    answer = []

    bundles = list(zip(progresses, speeds))
    day_lefts = [math.ceil((100 - bundle[0])/ bundle[1]) for bundle in bundles]

    count = 1
    for i in range(len(day_lefts) - 1):

        if day_lefts[i] < day_lefts[i + 1]:
            answer.append(count)
            count = 1
        else:
            day_lefts[i + 1] = day_lefts[i]
            count += 1

    answer.append(count)
    return answer

questions = [
    ([93, 30, 55], [1, 30, 5]),
    ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
]

result = solution_review(*questions[0])
print(result)