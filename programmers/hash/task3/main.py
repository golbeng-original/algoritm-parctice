'''
전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''

from typing import Dict, List
import collections

class TrieNode:

    def __init__(self, value:str = None):
        self.value = value
        self.completed = False
        self.children:List[TrieNode] = []

    def find_child(self, ch:str):
        
        children = list(filter(lambda e: e.value == ch, self.children))
        if not children:
            return None
        
        return children[0]

    @staticmethod
    def add(root, value:str):
        curr_node:TrieNode = root

        for idx, ch in enumerate(value):
            
            child_node = curr_node.find_child(ch)
            if not child_node:
                child_node = TrieNode(ch)
                curr_node.children.append(child_node)

            curr_node = child_node

        curr_node.completed = True

    @staticmethod
    def is_has_prefix(root):
        stack:List[TrieNode] = []
        stack.append(root)
        while stack:
            
            node = stack.pop()
            if node.completed == True and node.children:
                return False
            
            for child in node.children:
                stack.append(child)

        return True


def solution(phone_book:List[str]):

    root = TrieNode()
    for phone in phone_book:
        TrieNode.add(root, phone)

    return TrieNode.is_has_prefix(root)


# 시간 초과
def solution_2(phone_book:List[str]):

    phone_book = sorted(phone_book, key=lambda e: len(e))

    phone_map:Dict[str, List[str]] = {}
    for phone in phone_book:

        for ch in phone:
            if ch not in phone_map:
                continue

            for e in phone_map[ch]:
                if phone.startswith(e):
                    return False

        latest_ch = list(phone)[-1]
        if latest_ch not in phone_map:
            phone_map[latest_ch] = []
        
        phone_map[latest_ch].append(phone)

    return True

def solution_review(phone_book:List[str]):

    # 사전식 정렬이 필수 조건이다..
    phone_book.sort()
    for lhs, rhs in zip(phone_book, phone_book[1:]):
        if rhs.startswith(lhs):
            return False

    return True

    #phone_book.sort()
    #for i in range(len(phone_book) - 1):
    #    if phone_book[i + 1].find(phone_book[i]) == 0:
    #        return False

    #return True

result = solution_review(["123","456","789"])
print(result)