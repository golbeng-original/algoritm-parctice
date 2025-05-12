from dataclasses import dataclass
from typing import List, Set

@dataclass
class RepeatResult:
    left:int
    right:int

    @property
    def length(self):
        return self.right - self.left + 1


def findRepeatedDnaSequences(s: str) -> List[str]:
    length = len(s)

    def find_repaet(left:int, right:int):

        left_ch = s[left]
        right_ch = s[right]

        while left >= 0 and right < length:
            if left_ch != s[left] or right_ch != s[right]:
                break

            if (right - left + 1) > 10:
                break

            left -= 1
            right += 1
        
        return RepeatResult(left=left + 1, right=right - 1)


    def add_new_repeat(repeat_result:RepeatResult, max_length:int, output:Set[str]):
        
        if repeat_result.length < max_length:
            return False
        
        if repeat_result.length >= length:
            return False

        if repeat_result.length > max_length:
            output.clear()
            output.add(s[repeat_result.left:repeat_result.right + 1])
            max_length = repeat_result.length

        elif repeat_result.length == max_length:
            output.add(s[repeat_result.left:repeat_result.right + 1])

        return True

    max_length = 0
    output:Set[str] = set()
    for i in range(len(s) - 1):

        odd_result = find_repaet(i, i)
        if odd_result.length >= 10:
            if add_new_repeat(odd_result, max_length, output):
                max_length = odd_result.length


        even_result = find_repaet(i, i+1)
        if even_result.length >= 10:
            if add_new_repeat(even_result, max_length, output):
                max_length = even_result.length

    return list(output)

def findRepeatedDnaSequences_2(s:str) -> List[str]:
    
    if len(s) < 10:
        return []
    
    seen:Set[str] = set()
    repeated:Set[str] = set()

    left = 0
    while left < len(s) - 10 + 1:
        substring = s[left:left + 10]

        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)

        left+=1

    return list(repeated)

questions:List[str] = [
    'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
    'AAAAAAAAAAAAA',
    'AAAAAAAAAA',
    'GAGAGAGAGAGA'
]

# AAAAAAAAAA
# AAAAAAAAAA

# len = 12
# 12 - 10 : 2
# 0 1 2 3 4 5 6 7 8 9 10 11
# GAGAGAGAGAGA
# GAGAGAGAGA

for question in questions:
    output = findRepeatedDnaSequences_2(question)
    print(output)