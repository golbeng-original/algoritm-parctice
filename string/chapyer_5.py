'''
그룹 애너그램
'''

from typing import Dict, List, Tuple
from collections import defaultdict 

def my_solution(input:List[str]):

    organize_list = [ (element, ''.join( sorted(element) )) for element in input ]
    
    organize_group = defaultdict(list)

    for origin, key in organize_list:
        organize_group[key].append(origin)

    return list(organize_group.values())

if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = my_solution(input)
    print(result)