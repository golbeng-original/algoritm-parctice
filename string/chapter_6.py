'''
가장 긴 팰린드롬 부분 문자열
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Dict, List, Tuple
from collections import defaultdict 

from utils.performance import timer

@timer
def book_solution(input:str):
    # 중앙부터 퍼저 나가는??

    def expand(left:int, right:int):
        while left >= 0 and right < len(input) and input[left] == input[right]:
            left -= 1
            right += 1
        
        return input[left + 1:right]
    
    if len(input) < 2 or input == input[::-1]:
        return input

    result = ''
    for i in range(len(input) - 1):
        result = max(
            result,
            expand(i, i + 1), # 짝수개 체크
            expand(i, i + 2), # 홀수개 체크
            key=len
        )

    return result

@timer
def my_solution(input:str):

    ch_list = list(input)

    longest_string = ''
    for i in range(len(ch_list)):
        for j in range(i, len(ch_list)):

            substring = ''.join(ch_list[i:j+1])
            if substring == substring[::-1] and len(substring) > len(longest_string):
                longest_string = substring

    return longest_string

if __name__ == '__main__':
    inputs = [
        "babad", # 정답 : bab 또는 aba
        "cbbd", # 정답 : bb
        "racecar", # 정답 : racecar
        "abacdfgdcaba", # 정답 : aba
        "abacdfgdcabba", # 정답 : abba
        "abcdef", # 정답 : a, b, c, d, e 또는 f 중 하나
        "aaaaaa", # 정답 : aaaaaa
        "", # 정답 : ""
        "x", # 정답 : x
        "a!@#@!a", # 정답 : a!@#@!a
        "Aa", # 정답 : A 또는 a
        "abcbahelloollehxyz", # 정답 : abcba 또는 helloolleh
    ]

    for input in inputs:
        #result = my_solution(input)
        result = book_solution(input)
        print(result)
        #break