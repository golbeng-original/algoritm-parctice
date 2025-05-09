from dataclasses import dataclass
from typing import List

'''
0-1 배낭문제
'''

@dataclass
class Question:
    k:int
    values:List[List[int]] # [[weight, value]]

def solution(q:Question):

    row_max = len(q.values) + 1
    column_max = q.k + 1

    dp:List[List[int]] = [] * row_max
    for _ in range(row_max):
        dp.append([0] * column_max)

    # 물건의 갯수 (A, AB, ABC, ABCD, ...) 조합으로 생각해야 한다.
    for row_idx in range(1, row_max):

        # 배낭의 무게 0 ~ K까지
        for column_idx in range(1, column_max):
            
            stuff_idx = row_idx - 1
            stuff_weight = q.values[stuff_idx][0]

            stuff_value = 0
            if column_idx >= stuff_weight:
                stuff_value = q.values[stuff_idx][1]

            prev_value_1 = dp[row_idx - 1][column_idx]
            prev_value_2 = dp[row_idx - 1][column_idx - stuff_weight]

            dp[row_idx][column_idx] = max(
                prev_value_1,
                prev_value_2 + stuff_value
            )

    print(dp[row_max - 1][column_max -1])

    
if __name__ == '__main__':
    
    question = Question(
        k=15,
        values=[
            [12, 4], #A
            [1, 2], #B
            [4, 10], #C
            [1, 1], #D
            [2, 2], #E
        ]
    )

    solution(question)