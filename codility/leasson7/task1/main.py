from typing import List


def solution(S):
    
    stack = []
    mapping = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for ch in S:

        if ch not in mapping:
            stack.append(ch)
            continue
        
        if not stack or stack.pop() != mapping[ch]:
            return 0

    return 1 if not stack else 0

questions:List[str] = [
    '{[()()]}',
    '{{{{',
    '([)()]'
]

for question in questions:
    result = solution(question)
    print(result)