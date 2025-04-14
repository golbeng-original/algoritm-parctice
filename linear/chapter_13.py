'''
펠린드롬 연결 리스트
'''
import sys
import os
from typing import List
import collections

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import timer, ListNode 

@timer
def book_solution_1(input:str):

    head = ListNode.createByRaw(input)

    rev = None
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next

        rev, rev.next, slow = slow, rev, slow.next
    
    # 짝수개 일떄 체크
    if fast:
        slow = slow.next
    
    # 중간지점부터 rev(역 방향), slow(정 방향)의 값이 일치하는 체크
    while rev and rev.value == slow.value:
        slow, rev = slow.next, rev.next

    return not rev

'''
Runner 방식
- 링크드 리스트 방식에서 정확히 중간 값을 찾기에 좋다.

        1->2->3->2->1
fast    ^     ^     ^
slow    ^  ^  ^

        1->2->2->1->X
fast    ^     ^     ^
slow    ^  ^  ^
rev     1<-2
'''


@timer
def my_solution(input:str):

    head = ListNode.createByRaw(input)

    queue = collections.deque()
    while head is not None:
        queue.append(head.value)
        head = head.next

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False

    return True

if __name__ == '__main__':

    questions = [
        '1->2', # 정답 : False
        '1->2->3->2->1', # 정답 : True
        '1->2->3->4->5', # 정답 : False
        '1->2->3->4->5->4->3->2->1', # 정답 : True
        '1->2->3->4->5->6->7->8->9->10', # 정답 : False 
    ]

    for question in questions:
        #print(f'{question} => {my_solution(question)}')
        print(f'{question} => {book_solution_1(question)}')