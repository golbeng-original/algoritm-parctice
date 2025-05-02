class ListNode:

    def __init__(self, value:int, *, next = None):
        self.value:int = value
        self.next:ListNode = next

    def print(self):
        print(str(self))

    def __str__(self):
        output = ''

        curr = self
        while curr:
            output += str(curr.value)
            curr = curr.next
            if curr:
                output += '->'

        return output

    @staticmethod
    def createByRaw(raw:str):
        if not raw:
            return None
        
        elements = raw.split('->')

        head:ListNode = ListNode(-1)
        current_node:ListNode = head

        for element in elements:
            if element.lower() == 'null':
                break

            current_node.next = ListNode(int(element))
            current_node = current_node.next

        head = head.next
        return head