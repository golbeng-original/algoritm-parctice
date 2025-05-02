'''
두수의 덧셈
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 

def reverse_list(head:ListNode) -> ListNode:
    
    node, prev = head, None

    while node:
        next = node.next
        node.next = prev

        prev = node
        node = next
        
        #next, node.next = node.next, prev
        #prev, node = node, next

    return prev

def my_solution(left_raw:str, right_raw:str):
    
    left_node = ListNode.createByRaw(left_raw)
    right_node = ListNode.createByRaw(right_raw)

    head = ListNode(-1)
    current = head

    carry_value = 0 
    while left_node or right_node or carry_value > 0:

        left_value = left_node.value if left_node else 0
        right_value = right_node.value if right_node else 0

        digit_value = left_value + right_value + carry_value
        carry_value = digit_value // 10
        digit_value = digit_value % 10

        current.next = ListNode(digit_value)
        current = current.next

        if left_node:
            left_node = left_node.next
        
        if right_node:
            right_node = right_node.next

    head = head.next
    head = reverse_list(head)
    head.print()

if __name__ == '__main__':
    
    questions = [
        ['2->4->3' , '5->6->4'], # 7->0->8
        ['0' , '0'], # 0
        ['1->2->3' , '4->5->6'], # 5->7->9
        ['9->9->9' , '1'], # 0->0->0->1
        ['3->2->1' , '6->5->4'], # 9>7->5
        ['1->2->3' , '0->0->0'], # 1->2->3
        ['9->9->9' , '9->9->9'], # 8->9->9->1
    ]

    for question in questions:
        my_solution(question[0], question[1])
        