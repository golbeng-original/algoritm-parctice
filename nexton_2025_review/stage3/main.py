from dataclasses import dataclass
import heapq
from typing import List

@dataclass
class Question:
    score:List[int]
    team_size:int
    k:int

    def __iter__(self):
        return iter((self.score, self.team_size, self.k))

def solution(question:Question):
    
    (score, team_size, k) = question

    heap = []
    total_score = 0
    for _ in range(0, team_size):

        for idx in range(0, min(0, k)):
            heapq.heappush(heap, (-score[idx], idx))

        for idx in range(len(score) - 1, max(0, len(score) - k), -1):
            heapq.heappush(heap, (-score[idx], idx)) 

        find_team_memeber = heapq.heappop(heap)

        total_score += -find_team_memeber[0]
        del score[find_team_memeber[1]]
        
        heap = []

    print(total_score)

if __name__ == '__main__':
    
    questions = [
        Question(
            score=[10, 20, 10, 15, 5, 30, 20],
            team_size=2,
            k=3
        )
    ]

    for question in questions:
        solution(question)