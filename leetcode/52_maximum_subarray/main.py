
from typing import List
import sys


def solution(nums:List[int]) -> int:
    
    if len(nums) == 1:
        return nums[0]

    sums = [
        nums[0] if nums[0] > 0 else 0
    ]

    for idx in range(1, len(nums)):

        prev_sum = sums[idx - 1] if sums[idx - 1] > 0 else 0

        sums.append(
            nums[idx] + prev_sum 
        )

    return max(sums)

questions:List[List[int]] = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5,4,-1,7,8]
]

for question in questions:
    result = solution(question)
    print(result)
