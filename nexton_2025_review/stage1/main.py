
from typing import List

MAX = 10**5 + 1

def solution(operations:List[List[int]]):
    
    switchs = [0] * (MAX + 1)

    for operation in operations:
        left = operation[0]
        right = operation[1]

        switchs[left] += 1
        switchs[right + 1] -= 1

    total_value = 0
    curr_switch_state = 0
    for idx, switch in enumerate(switchs):
        
        curr_switch_state += switch
        if curr_switch_state % 2 == 1:
            total_value += idx

    print(f'result : {total_value}')

if __name__ == '__main__':
    question = [
        [1, 4],
        [2, 6],
        [1, 6]
    ]

    solution(question)
