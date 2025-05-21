
from typing import Set


def solution(S:str):
    
    def find_tree_div(value:str, idx:int) -> int:
        if idx >= len(value):
            return 0
        
        count = 0
        for num in range(10):
            div_value = value[0:idx] + str(num) + value[idx+1:]
            if int(div_value) % 3 == 0:
                print(f'divvalue : {div_value}, idx : {idx}')
                count +=1

        return count + find_tree_div(value, idx + 1)

    output = find_tree_div(S, 0)
    return output

questions = [
    #"23",
    "0081",
    #"022"
]

ss:Set[int] = set()

for question in questions:
    output = solution(question)
    print(output)