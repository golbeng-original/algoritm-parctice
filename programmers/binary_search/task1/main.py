'''
입국심사
https://school.programmers.co.kr/learn/courses/30/lessons/43238
'''

from typing import List

def solution(n:int, times:List[int]):
    answer = 0

    start = 1
    end = 1_000_000_000 * 100_000 # 심사관당 심사 시간 * 심사관 최대 수

    answer = 0
    while start <= end:

        middle = (start + end) // 2

        done_count = sum([middle //time for time in times])
        if done_count < n:
            start = middle + 1
        else:
            answer = middle
            end = middle - 1

    return answer

result = solution(6, [7,10])
print(result)