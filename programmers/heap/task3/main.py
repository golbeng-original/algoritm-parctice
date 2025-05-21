'''
이중 우선순위큐
https://school.programmers.co.kr/learn/courses/30/lessons/42628
'''

import heapq
from typing import List

class DoubleQueue:

    def __init__(self):
        self.queue = []

    def insert(self, value:int):
        
        temp = self.queue[:]
        self.queue = []
        
        heapq.heapify(temp)
        heapq.heappush(temp, value)
        while temp:
            self.queue.append(heapq.heappop(temp))
        
    def delete_max(self):
        if not self.queue:
            return
        
        self.queue.pop(-1)

    def delete_min(self):
        if not self.queue:
            return
        
        self.queue.pop(0)

    def peek(self):
        min = self.queue[0] if self.queue else 0
        max = self.queue[-1] if self.queue else 0
        
        return [max, min]

def solution(operations:List[str]):

    double_queue = DoubleQueue()
    for op in operations:
        inst, value = op.split(' ')

        if inst == 'I':
            double_queue.insert(int(value))
        elif inst == 'D' and value == '-1':
            double_queue.delete_min()
        elif inst == 'D' and value == '1':
            double_queue.delete_max()

    answer = double_queue.peek()
    return answer

result = solution(
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
)
print(result)