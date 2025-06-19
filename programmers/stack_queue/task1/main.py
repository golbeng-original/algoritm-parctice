'''
같은 숫자는 싫어
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''

def solution(arr):
    answer = []

    answer.append(arr[0])
    for e in arr[1:]:
        if answer[-1] == e:
            continue

        answer.append(e)

    return answer

questions = [
    [1,1,3,3,0,1,1],
    [4,4,4,3,3]
]

result = solution(questions[0])
print(result)