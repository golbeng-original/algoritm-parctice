
from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    X:int
    Y:int
    A:List[int]

def solution(question:Question):
    
    X = question.X
    Y = question.Y
    A = question.A

    x_count = 0
    y_count = 0
    max_idx = -1
    for idx, value in enumerate(A):

        if value == X:
            x_count += 1
        if value == Y:
            y_count += 1
        
        if x_count != 0 and x_count == y_count:
            max_idx = idx

    return max_idx



questions = [
    Question(
        X=7,
        Y=42,
        A=[6, 42, 11, 7, 1, 42]
    ),
    Question(
        X=6,
        Y=13,
        A=[13, 13, 1, 6]
    ),
    Question(
        X=100,
        Y=63,
        A=[100, 63, 1, 6, 2, 13]
    )
]

for question in questions:
    result = solution(question)
    print(result)