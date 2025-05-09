

from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    n:int
    k:int
    t:int
    start:List[int]
    finish:List[int]

    def __iter__(self):
        return iter((self.n, self.k, self.t, self.start, self.finish))

def solution(q:Question):
    
    (n, k, t, start, finish) = q

    def find_break_time(moved_start:List[int], moved_finish:List[int]):
        
        max_braek_time = moved_start[0]
        for i in range(1, n):

            if i == n - 1:
                max_braek_time = max(max_braek_time, t - moved_finish[i])
                continue

            max_braek_time = max(max_braek_time, moved_start[i] - moved_finish[i - 1])

        return max_braek_time

    ## idx 기준으로 이동을 해본다.
    def move_presentation(idx):

        temp_start = start[:]
        temp_finish = finish[:]

        moves = 0

        max_break_time = 0

        ## 앞쪽으로 k번 이동해본다.
        while idx < n and moves < k:
            gap = temp_finish[idx] - temp_start[idx]
            
            if idx == 0:
                temp_start[idx] = 0
            else:
                temp_start[idx] = temp_finish[idx - 1]

            temp_finish[idx] = temp_start[idx] + gap

            idx+=1
            moves+=1

        max_break_time = max(
            max_break_time,
            find_break_time(temp_start, temp_finish)
        )

        temp_start = start[:]
        temp_finish = finish[:]

        ## 뒤쪽으로 k번 이동해본다.
        while idx < n and moves < k:
            gap = temp_finish[idx] - temp_start[idx]
            
            if idx == n - 1:
                temp_finish[idx] = t
            else:
                temp_finish[idx] = temp_start[idx + 1]

            temp_start[idx] = temp_finish[idx] - gap

            idx+=1
            moves+=1

        max_break_time = max(
            max_break_time,
            find_break_time(temp_start, temp_finish)
        )

        return max_break_time


    max_break_time = 0
    for idx in range(n):
        max_break_time = max(
            max_break_time,
            move_presentation(idx)
        )

    print(max_break_time)


if __name__ == '__main__':
    
    questions = [
        Question(
            n=4,
            k=2,
            t=15,
            start=[4, 6, 7, 10],
            finish=[5, 7, 8, 11]
        ),
        Question(
            n=3,
            k=2,
            t=15,
            start=[0, 6, 7],
            finish=[5, 7, 8]
        )
    ]

    for question in questions:
        solution(question)