import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Tuple
from utils.performance import timer


'''
로그 파일 재정렬
'''

@timer
def book_solution(input:List[str]):

    letter_logs:List[str] = []
    digit_logs:List[str] = []

    for element in input:
        if element.split(' ')[1].isnumeric():
            digit_logs.append(element)
        else:
            letter_logs.append(element)
    
    letter_logs.sort(
        key=lambda x : (x.split()[1:], x.split()[0])
    )

    return letter_logs + digit_logs

@timer
def my_solution(input:List[str]):

    letter_logs:List[Tuple[str, str]] = []
    digit_logs = []
    for element in input:

        pivot_str = element.split(' ')[1]
        if pivot_str.isnumeric():
            digit_logs.append(element)
        else:
            letter_logs.append((element, pivot_str))

    result = []
    while len(letter_logs) > 0:

        # pivot 같은게 있나?
        origin, pivot_str = letter_logs.pop(0)

        result.append(origin)

        find_count = 0
        for idx, entry in enumerate(letter_logs):
            _, rest_pivot_str = entry
            if pivot_str == rest_pivot_str:
                letter_logs.insert(find_count, letter_logs.pop(idx))
                find_count += 1

    result.extend(digit_logs)

    return result

if __name__ == "__main__":
    
    inputs = [
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
        ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off KEY dog", "a8 act zoo"]
    ]
    
    for input in inputs:
        #result = my_solution(input)
        result = book_solution(input)
        print(result)