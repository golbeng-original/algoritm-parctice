'''
가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''

import functools

def solution_review(numbers):

    numbers = list(map(str, numbers))

    def compare(lhs, rhs):
        value_1 = lhs+rhs
        value_2 = rhs+lhs

        return 1 if int(value_1) < int(value_2) else -1
    
    numbers = sorted(numbers, key=functools.cmp_to_key(compare), reverse=False)

    answer = str(int(''.join(numbers)))
    return answer

def solution(numbers):

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x : x*3, reverse=True)

    value = int(''.join(numbers))
    answer = str(value)
    return answer


questions = [
    [6, 10, 2],
    [3, 30, 34, 5, 9]
]

result = solution_review(questions[0])
print(result)