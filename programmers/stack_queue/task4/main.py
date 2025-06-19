'''
프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''

import collections

def solution(priorities, location):
    answer = 0

    q = collections.deque()
    for loc, p in enumerate(priorities):
        q.append((p, loc))

    while q:
        max_prioprty = max(q, key=lambda x : x[0])
        value = q.popleft()
        if value[0] == max_prioprty[0]:
            answer += 1
            if value[1] == location:
                return answer
        
        else:
            q.append(value)


    return -1

questions = [
    ([2, 1, 3, 2], 2),
    ([1, 1, 9, 1, 1, 1], 0)
]

result = solution(*questions[0])
print(result)

'''
특정 프로세스가 몇번쨰로 실행되는지?

1. Queue에서 대기 중인 프로세스 꺼냄
2. 대기중인 프로세스 중 우선순위가 더 높은 프로세스 있음 다시 큐에 넣는다
3. 우선순위 높은게 없다면 방금 꺼낸 프로세스 실행
4. 한번 실행한 프로세스는 그대로 종료

[A, B, C , D], [2, 1, 3, 2]
->
[C, D, A, B]

1 <= N <= 100
'''