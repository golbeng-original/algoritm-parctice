'''
두 정렬 리스트의 병합
'''

import sys
import os
from typing import List
import collections

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 

@timer
def my_solution(input:List[str]):
    # 1순위 idx, 2순위 value
    left_node = ListNode.createByRaw(input[0])
    right_node = ListNode.createByRaw(input[1])

    head:ListNode = ListNode(-1)
    current_node:ListNode = head

    while left_node is not None and right_node is not None:

        value = None
        if left_node.value < right_node.value:
            value = left_node.value
            left_node = left_node.next
        else:
            value = right_node.value
            right_node = right_node.next
        
        current_node.next = ListNode(value)
        current_node = current_node.next

    while left_node:
        current_node.next = ListNode(left_node.value)
        current_node = current_node.next

        left_node = left_node.next

    while right_node:
        current_node.next = ListNode(right_node.value)
        current_node = current_node.next

        right_node = right_node.next

    head = head.next

    result = ''
    while head:
        result += head.value
        head = head.next
        if head:
            result += '->'

    return result

if __name__ == '__main__':
    questions = [
        ['1->2->4', '1->3->4'], # 정답 : 1->1->2->3->4->4
        ['1->2->4', '2->3->4'], # 정답 : 1->2->2->3->4->4
        ['1', '1'], # 정답 : 1->1
        ['1', '2'], # 정답 : 1->2
        ['1', ''], # 정답 : 1
        ['', ''], # 정답 : ''
    ]

    for question in questions:
        print(f'{question} => {my_solution(question)}')
        #print(f'{question} => {book_solution_1(question)}')