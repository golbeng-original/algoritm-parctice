

from typing import List


def solution(bit_arr:List[List[int]]) -> List[int]:

    def convert_to_decimal(bits:List[int]):
        value = 0
        for bit in bits:
            value += 1 << bit
        return value
    
    elements = [(convert_to_decimal(value), idx) for idx, value in enumerate(bit_arr)] 
    
    sorted_elements = sorted(
        elements,
        key=lambda e : e[0],
        reverse=True
    )

    print([element[1] for element in sorted_elements])

if __name__ == '__main__':
    qustions = [
        [0, 2],
        [2, 3],
        [2, 1]
    ]

    solution(qustions)