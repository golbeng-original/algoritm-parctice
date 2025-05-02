'''
페어의 노드 스왑
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 

def book_solution_1(input:str):

    head = ListNode.createByRaw(input)

    curr = head

    while curr and curr.next:

        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next

    head.print()

def book_solution_2(input:str):

    head = ListNode.createByRaw(input)
    root = prev = ListNode(0)

    prev.next = head

    while head and head.next:

        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next

    root = root.next
    root.print()

def book_solution_3(input:str):

    head = ListNode.createByRaw(input)

    def recursive(value_node:ListNode):

        if value_node and value_node.next:

            p = value_node.next
            value_node.next = recursive(p.next)
            p.next = value_node
            return p
        
        return value_node

    result = recursive(head)

    result.print()

def my_solution(input:str):

    root = ListNode(0)
    head = ListNode.createByRaw(input)
    
    prev, root.next = root, head

    while head and head.next:

        a = head
        b = head.next

        a.next = b.next
        b.next = a

        prev.next = b

        head = a.next
        prev = prev.next.next

    root = root.next
    root.print()


if __name__ == '__main__':

    questions = [
        '1->2->3->4', # 2->1->4->3
        '5->6->7->8->10', # 6->5->8->7->10
        '9->10->11', # 10->9->11
        '20->2', # 2->20
    ]

    for question in questions:
        #book_solution_2(question)
        book_solution_3(question)
        #my_solution(question)