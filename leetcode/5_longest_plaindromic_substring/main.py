from dataclasses import dataclass
from typing import List

@dataclass
class PalindromeResult:
    left:int
    right:int

    def __len__(self):
        return self.right - self.left + 1

def longestPalindrome(s: str) -> str:
    
    length = len(s)

    def check_palindrome(left:int, right:int) -> PalindromeResult:

        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1

        return PalindromeResult(left + 1, right - 1)


    start = 0
    end = 0
    max_len = 1
    for i in range(len(s)):
        
        odd_result = check_palindrome(i, i)
        even_result = check_palindrome(i, i + 1)

        select_result = odd_result if len(odd_result) > len(even_result) else even_result

        if len(select_result) > max_len:
            start = select_result.left
            end = select_result.right

            max_len = len(select_result)

    return s[start:end+1]


questions:List[str] = [
    'babad',
    'cbbd'
]

for question in questions:
    output = longestPalindrome(question)
    print(output)