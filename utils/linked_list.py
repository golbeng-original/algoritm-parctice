class ListNode:

    def __init__(self, value:int, *, next = None):
        self.value:int = value
        self.next:ListNode = next

    @staticmethod
    def createByRaw(raw:str):
        if not raw:
            return None
        
        elements = raw.split('->')

        prev:ListNode = None
        head:ListNode = None
        for element in elements[::-1]:
            prev = head
            head = ListNode(element, next=prev)

        return head