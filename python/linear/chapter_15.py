'''
역순 연결 리스트
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 

def my_solution(input:str):

    head = ListNode.createByRaw(input)

    def recursive(node:ListNode, prev:ListNode = None):
        if not node:
            return prev
        
        next, node.next = node.next, prev
        
        return recursive(next, node)

    new_head = recursive(head)
    new_head.print()


def my_solution_2(input:str):

    head = ListNode.createByRaw(input)

    def recursive(node:ListNode, prev:ListNode = None):
        if not node:
            return prev

        next = node.next # 2->3, 3, None
        node.next = prev  # 1->None, 2->1->None, 3->2->1->None

        return recursive(next, node)

    reverse_head:ListNode = recursive(head)

    reverse_head.print()

if __name__ == '__main__':
    questions = [
        '1->2->3->4->5->NULL',  # 5->4->3->2->1->NULL
        '6->7->8->9->10->NULL',  # 10->9->8->7->6->NULL
        '11->12->13->14->15->NULL',  # 15->14->13->12->11->NULL
    ]

    for question in questions:
        my_solution_2(question)