'''
주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for idx in range(len(prices)):
        while stack and prices[stack[-1]] > prices[idx]:
            top = stack.pop()
            answer[top] = idx - top

        stack.append(idx)

    for idx in stack:
        answer[idx] = len(prices) - 1 - idx

    return answer


questions = [
    [1, 2, 3, 2, 3]
]

result = solution(questions[0])
print(result)
