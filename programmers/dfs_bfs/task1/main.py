'''
타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

from typing import List


class Node:
    
    def __init__(self, curr_value:int = 0, is_minus:bool = False):
        self.__value = curr_value
        self.is_minus = is_minus

        self.childrens:List[Node] = []

    @property
    def value(self):
        if self.is_minus:
            return -self.__value
        
        return self.__value

def solution(numbers:List[int], target:int):

    def make_tree_node(numbers:List[int]):
        root = Node(0)

        next_children = [root]

        for i in range(len(numbers)):
            
            make_nodes = []
            generate_count = 2**(i+1)
            for j in range(generate_count):
                make_nodes.append(
                    Node(numbers[i], j % 2 == 0)
                )
            
            for j in range(len(next_children)):
                
                next_children[j].childrens.append(
                    make_nodes[j*2]
                )
                next_children[j].childrens.append(
                    make_nodes[j*2 + 1]
                )

            next_children = make_nodes[:]

        return root
    
    root_node = make_tree_node(numbers)

    answer = 0
    def dfs(node:Node, acc_value:int, target:int):
        nonlocal answer

        if len(node.childrens) == 0:
            answer += 1 if acc_value == target else 0
            return
        
        for child in node.childrens:
            dfs(child, acc_value + child.value, target)
    
    dfs(root_node, 0, target)

    return answer

def solution_dp(numbers:List[int], target:int):

    def dfs(remains:List[int], acc:int):

        if not remains and acc == target:
            return 1

        if not remains:
            return 0
        
        return dfs(remains[1:], acc + remains[0]) + dfs(remains[1:], acc - remains[0])
    
    answer = dfs(numbers, 0)
    return answer

result = solution_dp(
    [1, 1, 1, 1, 1],
    3
)

print(result)