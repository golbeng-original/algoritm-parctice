'''
N으로 표현
https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''

'''
점화식
d[1]    = N

-> 여기서부터 시작
d[2]    = d[1] & d[1] -> NN, N*N, N//N, N+N, N-N
d[3]    = d[2] & d[1] -> (N+N)N 
        = d[1] & d[2]
d[4]    = d[3] & d[1]
        = d[2] & d[2]
        = d[3] & d[1]
...
'''

from typing import List


def clac_attach_op_value(lhs_values:List[int], N:int):

    result_values = []
    for lhs_value in lhs_values:
        if lhs_value == N:
            result_values.append(lhs_value * 10 + N)

    return result_values

def calc_normal_op_value(lhs_values:List[int], rhs_values:List[int]):

    result_values = []
    for lhs_value in lhs_values:
        for rhs_value in rhs_values:

            # 더하기
            result_values.append(lhs_value + rhs_value)
            
            # 빼기
            minus_value = lhs_value - rhs_value
            if minus_value >= 0:
                result_values.append(lhs_value - rhs_value)

            # 곱하기
            result_values.append(lhs_value * rhs_value)
            # 나누기
            if rhs_value != 0:
                result_values.append(lhs_value // rhs_value)

    return result_values

MAX = 9
def solution(N:int, number:int):
    
    if N == number:
        return 1

    dp:List[List[int]] = [[] for _ in range(MAX)]
    dp[1].append(N)

    for i in range(2, MAX):
        # 2 : 1
        # 3 : 1, 2 -> (2 , 1), (1, 2)
        # 4 : 1, 2, 3
        
        #dp[j] = dp[j] op dp[i - j]

        # 붙이기 연산은 강제적으로
        dp[i].append(int(str(N) * i))
        for j in range(1, i):

            lhs_values = dp[i - j]
            rhs_values = dp[j]

            new_values = calc_normal_op_value(lhs_values, rhs_values)
            dp[i].extend(new_values)

        if number in dp[i]:
            return i

    return -1

result = solution(2, 11)
print(result)