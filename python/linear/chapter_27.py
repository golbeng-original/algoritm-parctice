'''
k개 정렬 리스트 병합
'''

import heapq
import sys
import os
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode

def book_solution(input:List[str]):
    
    list_nodes:List[ListNode] = []
    for element in input:
        list_nodes.append(ListNode.createByRaw(element))

    root = result = ListNode(-1)
    heap = []

    for i, list_node in enumerate(list_nodes):
        heapq.heappush(heap, (list_node.value, i, list_node))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.value, idx, result.next))

    root.next.print()

if __name__ == '__main__':
    
    questions = [
        [
            '1->4->5',
            '1->3->4',
            '2->6'
        ]
    ]

    for question in questions:
        book_solution(question)