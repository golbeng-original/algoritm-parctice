'''
가장 흔한 단어
'''
import re
from typing import List
from collections import defaultdict, Counter


def book_solution_1(paragraph:str, banned:List[str]):

    paragraph = paragraph.lower()

    paragraph = re.sub(r'[^\w]', ' ', paragraph)

    elements = [element for element in paragraph.split() if element not in banned ]

    word_mapping = defaultdict(int)
    for element in elements:
        word_mapping[element] += 1

    return max(word_mapping, key=word_mapping.get)

def book_solution_2(paragraph:str, banned:List[str]):

    paragraph = paragraph.lower()

    paragraph = re.sub(r'[^\w]', ' ', paragraph)

    elements = [element for element in paragraph.split() if element not in banned ]

    counter = Counter(elements)

    return counter.most_common(1)[0][0]

def my_solution(paragraph:str, banned:List[str]):

    paragraph = paragraph.lower()

    paragraph = re.sub(r'[^\w]', ' ', paragraph)

    elements = [element for element in paragraph.split() if element not in banned ]

    word_mapping = defaultdict(int)
    for element in elements:
        word_mapping[element] += 1

    order_words = [ item for item in word_mapping.items() ]
    order_words.sort(
        key=lambda x : (x[1]),
        reverse=True
    )

    return order_words[0][0]

if __name__ == '__main__':

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]


    #result = my_solution(paragraph, banned)
    #result = book_solution_1(paragraph, banned)
    result = book_solution_2(paragraph, banned)
    print(result)