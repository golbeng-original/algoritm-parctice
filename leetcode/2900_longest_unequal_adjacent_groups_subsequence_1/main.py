from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    words:List[str]
    groups:List[int]


class Solution:
    
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []
        
        length = len(words)

        result:List[str] = words[0:1]
        prev = groups[0]

        for i in range(1, length):
            if prev != groups[i]:
                prev = groups[i]
                result.append(words[i])

        return result


questions = [
    Question(
        words=['e', 'a', 'b'],
        groups=[0, 0, 1]
    ),
    Question(
        words=['a','b','c','d'],
        groups=[1,0,1,1]
    )
]

for question in questions:
    solution = Solution()
    result = solution.getLongestSubsequence(question.words, question.groups)
    print(result)