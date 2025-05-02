'''
홀짝 연결 리스트
- 홀수번쨰 끼리, 짝수번쨰 끼리 묶음
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 


def book_solution_1(input:str):

    head = ListNode.createByRaw(input)

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:

        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    
    odd.next = even_head

    head.print()


def my_solution(input:str):
    head = ListNode.createByRaw(input)

    prev_odd:ListNode = head
    curr_odd:ListNode = head
    even_head_node = curr_even = head.next

    ## 홀수 기준으로 구함
    while curr_odd:
        next_odd = None
        if curr_odd.next and curr_odd.next.next:
            next_odd = curr_odd.next.next

        curr_odd.next = next_odd
        prev_odd = curr_odd
        curr_odd = curr_odd.next

        ## 
        next_even = None
        if curr_even and curr_even.next and curr_even.next.next:
            next_even = curr_even.next.next

        if curr_even:
            curr_even.next = next_even
            curr_even = curr_even.next

    prev_odd.next = even_head_node

    head.print()


if __name__ == '__main__':
    
    # 다양한 테스트 케이스
    questions = [
        '1->2->3->4->5',        # 1->3->5->2->4
        '2->1->3->5->6->4->7',  # 2->3->6->7->1->5->4
    ]

    for question in questions:
        print(f'question: {question}')
        #my_solution(question)
        book_solution_1(question)