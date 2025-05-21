'''
소수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''

from typing import List


def solution(numbers):

    def check_prime(value:int):
        if value < 2:
            return False
        
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                return False
            
        return True

    prime_count = 0
    checked_number = set()
    def backtracking(curr_str:List[str], remain:List[str]):
        nonlocal prime_count

        if curr_str:
            value = int(''.join(curr_str))
            if value not in checked_number:
                checked_number.add(value)

                if check_prime(value):
                    prime_count += 1
            
        
        if not remain:
            return

        for idx, ch in enumerate(remain):
            backtracking(curr_str + [ch], remain[0:idx] + remain[idx+1:])

            
    
    splits_numbers = [ch for ch in numbers]
    backtracking([], splits_numbers)

    return prime_count


result = solution('011')
print(result)