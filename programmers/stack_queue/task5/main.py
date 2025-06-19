'''
다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''

from typing import List


def solution(bridge_length:int, weight:int, truck_weights:List[int]):
    answer = 0

    timer = 0
    bridge = []
    curr_bridge_weight = 0
    while truck_weights or bridge:
        timer += 1
        
        if bridge and timer == bridge[0][0]:
            curr_truck = bridge.pop(0)
            curr_bridge_weight -= curr_truck[1]
            

        if len(bridge) < bridge_length and \
            truck_weights and \
            curr_bridge_weight + truck_weights[0] <= weight:

            curr_weight = truck_weights.pop(0)
            curr_bridge_weight += curr_weight
            bridge.append((timer+bridge_length, curr_weight))

    return timer

questions = [
    (2, 10, [7,4,5,6]),
    (100, 100, [10]),
    (100, 100, [10,10,10,10,10,10,10,10,10,10]),
]

result = solution(*questions[2])
print(result)