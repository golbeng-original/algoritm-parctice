'''
올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer = True
    
    stack = []
    for ch in s:
        
        if ch == '(':
            stack.append(ch)
        elif ch == ')':

            if len(stack): 
                stack.pop()
            else:
                return False

    return False if len(stack) > 0 else True

questions = [
    '()()',
    '(())()',
    '(()('
]

result = solution(questions[0])
print(result)