import re
import time
from collections import deque
from typing import Deque

def book_solution_1(input:str):
    
    question = input.lower()
    question = [ch for ch in question if ch.isalnum()]

    while len(question) > 1:
        if question.pop() != question.pop(0):
            return False

    return True

def book_solution_2(input:str):
    question = input.lower()
    
    strs:Deque = deque()
    for ch in question:
        if ch.isalnum():
            strs.append(ch)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def book_solution_3(input:str):

    question = input.lower()
    question = [ch for ch in question if ch.isalnum()]

    return question == question[::-1]

def my_solution(input:str):
    
    # 앞에서 시작
    # 뒤에서 시작

    question = input.lower()
    question = [ch for ch in question if ch.isalnum()]

    i = 0
    j = len(question) - 1
    while i < j:

        left_char = question[i]
        right_char = question[j]

        if left_char != right_char:
            return False
        
        i += 1
        j -= 1

    return True

if __name__ == "__main__":
    input = 'A man, a plan, a canal: Panama'
    #input = 'race a car'

    begin_time = time.time_ns()

    #result = my_solution(input) # 8ms
    #result = book_solution_1(input) # 8ms

    #result = book_solution_2(input) # 15ms
    result = book_solution_3(input) # 4ms


    during_time = time.time_ns() - begin_time

    print(f'result : {result}, [{during_time/1000} ms]')