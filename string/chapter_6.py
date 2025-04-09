'''
가장 긴 팰린드롬 부분 문자열
'''

from typing import Dict, List, Tuple
from collections import defaultdict 

def my_solution(input:List[str]):

    pass

if __name__ == '__main__':
    input = [
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
    result = my_solution(input)
    print(result)