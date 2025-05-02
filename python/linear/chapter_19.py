'''
역순 연결 리스트 2
 - m 에서 n 까지를 역순으로 만들기
 - m은 1부터 시작
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 


def my_solution(list:str, m:int, n:int):

    start = root = ListNode(-1)
    head = ListNode.createByRaw(list)

    root.next = head

    for _ in range(m - 1):
        start = start.next

    end = start.next
    for _ in range(n - m):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next

        start.next.next = tmp

    root = root.next
    root.print()


if __name__ == '__main__':
    
    questions = [
        ['1->2->3->4->5', 2, 4], # 1->4->3->2->5
        ['1->2->3->4->5', 1, 5], # 5->4->3->2->1
        ['1->2->3->4->5', 2, 5], # 5->4->3->2->1
        ['1', 1, 1], # 1
    ]

    for question in questions:
        print(f'input: {question[0]}, m: {question[1]}, n: {question[2]}')
        my_solution(question[0], question[1], question[2])

